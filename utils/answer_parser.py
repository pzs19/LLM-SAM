import re
import json

def extract_json(text):

    json_substrings = []
    stack = []
    start_idx = None

    for i, char in enumerate(text):
        if char == '{':
            if not stack:
                start_idx = i
            stack.append(char)
        elif char == '}':
            if stack:
                stack.pop()
                if not stack:
                    json_str = text[start_idx:i+1]
                    json_substrings.append(json_str)
    for candidate in json_substrings:
        try:
            json_obj = json.loads(candidate)
            assert "Opinion" in json_obj and "Decision" in json_obj
            return json_obj
        except Exception as e:
            print(e)
    raise ValueError(f"no valid answer")