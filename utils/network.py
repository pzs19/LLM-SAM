import numpy as np
from .answer_parser import extract_json
from .prompt_manager import PromptManager
from vllm import SamplingParams, LLM
import copy
import json
import random
import copy

NAMES = ["James", "Michael", "David", "Emily", "Sarah"]
N_MAX_RETRY = 3
class Node:
    def __init__(self, exp_id, n_node, person_id, coeff_df, llm, name, prompt_root):
        self.n_node = n_node
        self.person_id = person_id
        self.name = name
        self.llm = llm

        self.person_attr = {}
        attr_names = ["a", "tau", "f", "lambda", "O_inital_text", "O_inital", "A_inital"]
        for attr_name in attr_names:
            self.person_attr[attr_name] = coeff_df.loc[person_id, attr_name]
            if attr_name == "A_inital":
                self.person_attr[attr_name] = float(coeff_df.loc[person_id, attr_name])

        self.prompt_manager = PromptManager(exp_id, n_node, person_id % n_node, self.person_attr, name, prompt_root)
        self.opinion = {}
        self.opinion_history = []
        
    def set_opinion(self, opinion):
        """Sets the node's opinion with opinion and explanation."""
        assert isinstance(opinion, dict) and "Opinion" in opinion and "Decision" in opinion
        self.opinion = opinion
        self.opinion_history.append(copy.deepcopy(opinion))

    def get_prompt(self, step, neighbors_opinions=""):
        return self.prompt_manager.get_prompt(step, neighbors_opinions)
    
    def __call__(self, step, seed, neighbors_opinions="", do_free_chat=False):
        """Generate an opinion based on a prompt."""
        if step == 0:
            self.opinion = self.prompt_manager.get_initial_opinion()
            self.opinion_history.append(self.opinion)
            return self.opinion
        if do_free_chat:
            prompt = self.prompt_manager.get_chat_prompt(neighbors_opinions)
        else:
            prompt = self.prompt_manager.get_prompt(step, neighbors_opinions)
        valid = False
        for i in range(N_MAX_RETRY):
            if isinstance(self.llm, LLM):
                outputs = self.llm.generate(
                    prompt, 
                    SamplingParams(temperature=1, top_p=1.0, max_tokens=256, seed=seed+i*1000, stop=["# R"])
                )
                response = outputs[0].outputs[0].text
            else:
                outputs = self.llm(prompt)
                response = outputs["response"]
            try:
                self.opinion = extract_json(response)
                thought = self.opinion["Thought"]
                opinion = int(self.opinion["Opinion"])
                decision = self.opinion["Decision"]
                assert decision.lower() in ["yes", "no"] and opinion >= 0 and opinion <= 10
                self.opinion = {"Thought": thought, "Opinion": opinion, "Decision": decision}
                valid = True
                break
            except Exception:
                print(f'Invalid respose (retry={i}):\nInput:{prompt}\nOutput:\n{response}')
                print('='*100)
                continue
        if not valid:
            print(f'Invalid response, using previous opinion and decison.')
            self.opinion = self.opinion_history[-1]
        self.opinion_history.append(copy.deepcopy(self.opinion))
        return self.opinion

    def get_opinion(self, step):
        if step < 0:
            return ""
        assert step < len(self.opinion_history), f"index opinion history out of range, step {step} >= {len(self.opinion_history)}"
        opinion = self.opinion_history[step]
        return opinion

    def get_opinion_text_json(self, step):
        if step < 0:
            return ""
        assert step < len(self.opinion_history), f"index opinion history out of range, step {step} >= {len(self.opinion_history)}"
        opinion = self.opinion_history[step]
        if (not isinstance(opinion, dict)) or "Opinion" not in opinion or opinion["Opinion"] == -1:
            opinion_text = ""
        else:
            try:
                opinion_text = f"{self.name}'s ouput is {json.dumps(opinion, ensure_ascii=False)}"
            except Exception as e:
                print(e)
                opinion_text = ""
        return opinion_text
    
class SocialNetwork:
    def __init__(self, exp_id, n_node, st_person_id, coeff_df, llm, prompt_root, load_adj_mat_from=""):
        if n_node < len(NAMES):
            self.names = NAMES[:n_node]
        else:
            self.names = [f"User{i}" for i in range(n_node)]
        
        self.network = {
            name: Node(
                exp_id,
                n_node, 
                st_person_id+idx,
                coeff_df,
                llm,
                name,
                prompt_root
            ) for idx, name in enumerate(self.names)
        }
        self.size = len(self.names)
        self.adj_mat = np.ones((self.size, self.size)).astype(int)
        self.load_adj_mat_from = load_adj_mat_from
        if self.load_adj_mat_from:
            self.adj_mat_ori = np.load(self.load_adj_mat_from).astype(int)

        self.llm = llm
    
    def set_adj_mat(self, step=-1):
        if self.adj_mat_ori.ndim > 2:
            self.adj_mat = self.adj_mat_ori[step]
        else:
            self.adj_mat = self.adj_mat_ori

    def simulate(self, step, seed=42, enable_p2p=True, do_free_chat=False):
        """Generates opinions for all nodes based on a prompt and updates the buffer."""
        if do_free_chat:
            assert enable_p2p, "For free chat, must enable p2p"
        if self.load_adj_mat_from:
            self.set_adj_mat(step)
        for name in self.network.keys():
            if enable_p2p and step > 0:
                neighbors_opinions = "\n".join([self.network[n].get_opinion_text_json(step-1) for n in self.get_neighbors(name)])
                self.network[name](step, seed, neighbors_opinions, do_free_chat)
            else:
                self.network[name](step, seed,)

    def get_neighbors(self, name):
        """Gets neighbors of a person based on the adjacency matrix."""
        index = list(self.network.keys()).index(name)
        return [list(self.network.keys())[i] for i in range(self.size) if self.adj_mat[index, i] == 1]
    
    def get_opinions(self, ):
        opinions = {}
        for name, node in self.network.items():
            opinions[name] = node.opinion
        return opinions
    
    def get_opinion_history(self, ):
        opinions = {}
        for name, node in self.network.items():
            opinions[name] = {}
            opinions[name]["profile"] = node.person_attr
            opinions[name]["opinion"] = node.opinion_history
        return opinions