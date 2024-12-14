#!/bin/sh

python main.py \
    --model-name-or-path meta-llama/Meta-Llama-3.1-8B-Instruct \
    --load-adj-mat-from config/adj_mat/BA_dynamic.npy \
    --num-question 10 \
    --step-size 20 \
    --n-nodes "50" \
    --enable-free-chat \
    --prompt-dir prompt/prompt_3ex \
    --save-dir ../result_release/exp_init-op_3ex_50node_dynamic/Meta-Llama-3.1-8B-Instruct
python main.py \
    --model-name-or-path meta-llama/Meta-Llama-3.1-8B-Instruct \
    --load-adj-mat-from config/adj_mat/BA_50.npy \
    --num-question 3 \
    --step-size 20 \
    --n-nodes "50" \
    --prompt-dir prompt/prompt_3ex \
    --save-dir ../result_release/exp_init-op_3ex_50node_static/Meta-Llama-3.1-8B-Instruct

python main.py \
    --model-name-or-path Qwen/Qwen2.5-7B-Instruct \
    --load-adj-mat-from config/adj_mat/BA_dynamic.npy \
    --num-question 10 \
    --step-size 20 \
    --n-nodes "50" \
    --enable-free-chat \
    --prompt-dir prompt/prompt_3ex \
    --save-dir ../result_release/exp_init-op_3ex_50node_dynamic/Qwen2.5-7B-Instruct
python main.py \
    --model-name-or-path Qwen/Qwen2.5-7B-Instruct \
    --load-adj-mat-from config/adj_mat/BA_50.npy \
    --num-question 3 \
    --step-size 20 \
    --n-nodes "50" \
    --prompt-dir prompt/prompt_3ex \
    --save-dir ../result_release/exp_init-op_3ex_50node_static/Qwen2.5-7B-Instruct

python main.py \
    --model-name-or-path openai/gpt-4o-mini-2024-07-18 \
    --load-adj-mat-from config/adj_mat/BA_dynamic.npy \
    --num-question 10 \
    --step-size 20 \
    --n-nodes "50" \
    --enable-free-chat \
    --prompt-dir prompt/prompt_3ex \
    --save-dir ../result_release/exp_init-op_3ex_50node_dynamic/gpt-4o-mini-2024-07-18
python main.py \
    --model-name-or-path openai/gpt-4o-mini-2024-07-18 \
    --load-adj-mat-from config/adj_mat/BA_50.npy \
    --num-question 3 \
    --step-size 20 \
    --n-nodes "50" \
    --prompt-dir prompt/prompt_3ex \
    --save-dir ../result_release/exp_init-op_3ex_50node_static/gpt-4o-mini-2024-07-18