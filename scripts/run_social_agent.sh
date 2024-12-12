#!/bin/sh

python main.py \
    --model-name-or-path meta-llama/Meta-Llama-3.1-8B-Instruct \
    --prompt-dir prompt/prompt_3ex \
    --save-dir ../result_release/exp_init-op_3ex/Meta-Llama-3.1-8B-Instruct
    
python main.py \
    --model-name-or-path Qwen/Qwen2.5-7B-Instruct \
    --prompt-dir prompt/prompt_3ex \
    --save-dir ../result_release/exp_init-op_3ex/Qwen2.5-7B-Instruct

python main.py \
    --model-name-or-path openai/gpt-4o-mini-2024-07-18 \
    --prompt-dir prompt/prompt_3ex \
    --save-dir ../result/exp_init-op_3ex/gpt-4o-mini-2024-07-18