import os
import os.path as osp
from time import sleep
from dotenv import load_dotenv
from datetime import datetime

class OpenAILLM:
    def __init__(self, model_name="gpt-4o-mini-2024-07-18"):
        from openai import OpenAI
        self.model_name = model_name
        load_dotenv(osp.expanduser("~/dot_env/openai.env"))

        self.client = OpenAI()
        self.client.base_url = os.getenv("OPENAI_API_BASE")
        keys = os.getenv("OPENAI_API_KEY")
        self.client.api_key = keys.split(",")[0]

    def __call__(self, 
        prompt,
        *,
        system_prompt=None,
        temperature=0.7,
        max_tokens=512,
        max_num_retries=2,
        return_full=True,
    ) -> str:
        if system_prompt is not None:
            messages = [{
                "role": "system",
                "content": system_prompt,
            }, {
                "role": "user",
                "content": prompt,
            }]
        else:
            messages = [{
                "role": "user",
                "content": prompt,
            }]

        retry = 0
        while retry < max_num_retries:
            try:
                completion = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                content = completion.choices[0].message.content
                if not return_full:
                    return content

                ret_dict = {
                    "prompt": prompt,
                    "system_prompt": system_prompt,
                    "model_name": self.model_name,
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                    "response": content,
                    "response_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    # "completion_obj": completion,
                }
                return ret_dict

            except Exception as e:
                retry += 1
                sleep(5)
                print(f"Error: {e}", flush=True)

        raise RuntimeError('Calling OpenAI failed after retrying for '
                        f'{retry} times.')