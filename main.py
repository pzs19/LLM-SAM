import argparse
import os
import json
from utils.network import SocialNetwork
from utils.call_llm import OpenAILLM
import pandas as pd
from vllm import LLM 

def main(args):
    save_dir = args.save_dir
    os.makedirs(args.save_dir, exist_ok=True)

    if os.path.dirname(args.model_name_or_path) == "openai":
        llm = OpenAILLM(os.path.basename(args.model_name_or_path))
    else:
        model_path = os.path.join(args.model_dir, args.model_name_or_path) if args.model_dir else args.model_name_or_path
        llm = LLM(
            model_path,
            tensor_parallel_size=args.tp_size,
            dtype="bfloat16",
            trust_remote_code=True
        )

    n_nodes = list(map(int, args.n_nodes.split(",")))
    exp_ids = list(map(int, args.exp_ids.split(",")))
    for exp_id in exp_ids:
        all_results = {}
        exp_save_dir = os.path.join(save_dir, f"exp{exp_id}")
        os.makedirs(exp_save_dir, exist_ok=True)

        for n_node in n_nodes:
            n_node_save_dir = os.path.join(exp_save_dir, f"simulations_n{n_node}")
            os.makedirs(n_node_save_dir, exist_ok=True)
            coeff_df = pd.read_csv(f'{args.config_dir}/coeff{exp_id}_{n_node}.csv')
            step_size = args.step_size if args.step_size > 0 else n_node
            for st_person_id in range(0, coeff_df.shape[0]-n_node+1, step_size):
                res_path = os.path.join(n_node_save_dir, f"result_person{st_person_id}-{st_person_id+n_node}.json")
                if os.path.exists(res_path):
                    res = json.load(open(res_path, "r", encoding="utf-8"))
                    all_results[f"exp={exp_id},n={n_node},person={st_person_id}-{st_person_id+n_node}"] = res
                    print(f'exp={exp_id},n={n_node},person={st_person_id}-{st_person_id+n_node} exists, continue.')
                    continue
                results = []
                for seed in range(args.num_simulation):
                    social_network = SocialNetwork(
                        exp_id=exp_id, 
                        n_node=n_node, 
                        st_person_id=st_person_id, 
                        coeff_df=coeff_df, 
                        llm=llm, 
                        prompt_root=args.prompt_dir,
                        load_adj_mat_from=args.load_adj_mat_from,
                    )
                    for step in range(args.num_question):
                        if args.enable_free_chat and step >= 2 and step < (args.num_question - 1):
                            social_network.simulate(step, seed=seed, enable_p2p=args.enable_p2p, do_free_chat=True)
                        else:
                            social_network.simulate(step, seed=seed, enable_p2p=args.enable_p2p)
    
                    opinion_history = social_network.get_opinion_history()
                    os.makedirs(os.path.join(n_node_save_dir, "seed"), exist_ok=True)
                    json.dump(
                        opinion_history,
                        open(os.path.join(n_node_save_dir, "seed", f"result_seed{seed}_person{st_person_id}-{st_person_id+n_node}.json"), "w", encoding="utf-8"), 
                        indent=4, 
                        ensure_ascii=False
                    )
                    results.append(opinion_history)
                    break

                all_results[f"exp={exp_id},n={n_node},person={st_person_id}-{st_person_id+n_node}"] = results
                json.dump(
                    results,
                    open(os.path.join(n_node_save_dir, f"result_person{st_person_id}-{st_person_id+n_node}.json"), "w", encoding="utf-8"), 
                    indent=4, 
                    ensure_ascii=False
                )
                break

        json.dump(all_results, open(os.path.join(exp_save_dir, f"result_all.jsonl"), "w", encoding="utf-8"), indent=4, ensure_ascii=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--tp-size', type=int, default=1,
    )
    parser.add_argument(
        '--model-dir', type=str, default="",
    )
    parser.add_argument(
        '--num-simulation', type=int, default=5,
    )
    parser.add_argument(
        '--num-question', type=int, default=3,
    )
    parser.add_argument(
        '--step-size', type=int, default=0,
    )
    parser.add_argument(
        '--n-nodes', type=str, default="3,4,5",
    )
    parser.add_argument(
        '--exp-ids', type=str, default="1,2,3",
    )
    parser.add_argument(
        '--prompt-dir', type=str, default="prompt",
    )
    parser.add_argument(
        '--model-name-or-path', type=str, default="meta-llama/Meta-Llama-3.1-8B-Instruct",
    )
    parser.add_argument(
        '--save-dir', type=str, default="../result/exp_1023/llama3_1",
    )
    parser.add_argument(
        '--config-dir', type=str, default="config/coeff_with_init_op",
    )
    parser.add_argument(
        '--load-adj-mat-from', type=str, default="",
    )
    parser.add_argument(
        '--enable-p2p', action=argparse.BooleanOptionalAction, default=True
    )
    parser.add_argument(
        '--enable-free-chat', action=argparse.BooleanOptionalAction, default=False
    )
    parser.add_argument(
        '--verbose', action=argparse.BooleanOptionalAction, default=False
    )
    args = parser.parse_args()
    
    main(args)