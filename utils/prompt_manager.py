import os
import json

class PromptManager:
    def __init__(self, exp_id, n_node, rounded_person_id, person_attr, name, prompt_root="prompt"):
        self.exp_id = exp_id
        self.rounded_person_id = rounded_person_id
        self.n_node = n_node
        self.prompt_dir = f"{prompt_root}/exp{self.exp_id}"
        self.basic_info = self._load_json('basic_info.json')
        self.person_attr = person_attr

        background = self._load_md('background.md')
        background = background.replace("{name}", name)
        background = background.replace("{n_friend}", str(self.n_node))
        background = background.replace("{a}", str(self.person_attr["a"]))
        background = background.replace("{tau}", str(self.person_attr["tau"]))
        background = background.replace("{f}", str(self.person_attr["f"]))
        background = background.replace("{lambda}", str(self.person_attr["lambda"]))

        info_key = f"Basic Information {self.rounded_person_id+1}"
        basic_info_text = self.basic_info.get(info_key, "")
        background = background.replace("{basic_information}", basic_info_text)

        self.questions = self._load_questions()
        self.chat_template = self._load_chat_template()
        
        self.init_op = {
            "Thought": str(self.person_attr["O_inital_text"]), 
            "Opinion": int(self.person_attr['O_inital'] * 10),
            "Decision": "No" if abs(float(self.person_attr['A_inital']) - 0) < 1e-3 else "Yes",
        }
        self.init_ans = json.dumps(self.init_op, ensure_ascii=False)
        self.prefix_prompt = "\n".join([background, self.questions[0], self.init_ans])
        
    def _load_md(self, filename):
        filepath = os.path.join(self.prompt_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()

    def _load_json(self, filename):
        filepath = os.path.join(self.prompt_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)

    def _load_questions(self):
        questions = []
        for i in range(1, 4):
            question_filename = f'Q{i}.md'
            filepath = os.path.join(self.prompt_dir, question_filename)
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as file:
                    questions.append(file.read())
        return questions

    def _load_chat_template(self):
        filepath = os.path.join(self.prompt_dir, "free_chat.md")
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as file:
                chat_template = file.read()
        else:
            chat_template = ""
        return chat_template

    def get_chat_prompt(self, neighbors_opinions=""):
        chat_template = self.chat_template.replace("{neighbors_opinions}", neighbors_opinions)
        return self.prefix_prompt + "\n\n" + chat_template

    def get_prompt(self, step, neighbors_opinions=""):
        if step >= len(self.questions):
            q = self.questions[-1].replace("{neighbors_opinions}", neighbors_opinions)
        else:
            q = self.questions[step].replace("{neighbors_opinions}", neighbors_opinions)
        self.prefix_prompt += "\n" + q
        
        return self.prefix_prompt

    def get_initial_opinion(self):
        return self.init_op