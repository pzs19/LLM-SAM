#!/bin/sh

python main.py \
    --model-name-or-path meta-llama/Meta-Llama-3.1-8B-Instruct \
    --load-adj-mat-from config/adj_mat/BA.npy \
    --step-size 10 \
    --n-nodes "101" \
    --prompt-dir prompt/prompt_3ex \
    --save-dir ../result_release/exp_init-op_3ex_101node_BA/Meta-Llama-3.1-8B-Instruct 
python main.py \
    --model-name-or-path meta-llama/Meta-Llama-3.1-8B-Instruct \
    --load-adj-mat-from config/adj_mat/WS.npy \
    --step-size 10 \
    --n-nodes "101" \
    --prompt-dir prompt/prompt_3ex \
    --save-dir ../result_release/exp_init-op_3ex_101node_WS/Meta-Llama-3.1-8B-Instruct 
python main.py \
    --model-name-or-path meta-llama/Meta-Llama-3.1-8B-Instruct \
    --load-adj-mat-from config/adj_mat/ER.npy \
    --step-size 10 \
    --n-nodes "101" \
    --prompt-dir prompt/prompt_3ex \
    --save-dir ../result_release/exp_init-op_3ex_101node_ER/Meta-Llama-3.1-8B-Instruct

python main.py \
    --model-name-or-path Qwen/Qwen2.5-7B-Instruct \
    --load-adj-mat-from config/adj_mat/BA.npy \
    --step-size 10 \
    --n-nodes "101" \
    --prompt-dir prompt/prompt_3ex \
    --save-dir ../result_release/exp_init-op_3ex_101node_BA/Qwen2.5-7B-Instruct 
python main.py \
    --model-name-or-path Qwen/Qwen2.5-7B-Instruct \
    --load-adj-mat-from config/adj_mat/WS.npy \
    --step-size 10 \
    --n-nodes "101" \
    --prompt-dir prompt/prompt_3ex \
    --save-dir ../result_release/exp_init-op_3ex_101node_WS/Qwen2.5-7B-Instruct 
python main.py \
    --model-name-or-path Qwen/Qwen2.5-7B-Instruct \
    --load-adj-mat-from config/adj_mat/ER.npy \
    --step-size 10 \
    --n-nodes "101" \
    --prompt-dir prompt/prompt_3ex \
    --save-dir ../result_release/exp_init-op_3ex_101node_ER/Qwen2.5-7B-Instruct

python main.py \
    --model-name-or-path openai/gpt-4o-mini-2024-07-18 \
    --load-adj-mat-from config/adj_mat/BA.npy \
    --step-size 10 \
    --n-nodes "101" \
    --prompt-dir prompt/prompt_3ex \
    --save-dir ../result_release/exp_init-op_3ex_101node_BA/gpt-4o-mini-2024-07-18 
python main.py \
    --model-name-or-path openai/gpt-4o-mini-2024-07-18 \
    --load-adj-mat-from config/adj_mat/WS.npy \
    --step-size 10 \
    --n-nodes "101" \
    --prompt-dir prompt/prompt_3ex \
    --save-dir ../result_release/exp_init-op_3ex_101node_WS/gpt-4o-mini-2024-07-18 
python main.py \
    --model-name-or-path openai/gpt-4o-mini-2024-07-18 \
    --load-adj-mat-from config/adj_mat/ER.npy \
    --step-size 10 \
    --n-nodes "101" \
    --prompt-dir prompt/prompt_3ex \
    --save-dir ../result_release/exp_init-op_3ex_101node_ER/gpt-4o-mini-2024-07-18
