import pandas as pd
from peft import PeftModel, PeftConfig
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, GenerationConfig, TrainingArguments, Trainer
import torch
from loguru import logger

lora_model_path="lora_model1/"
lora_base_path = "google/flan-t5-small"


peft_model_base = AutoModelForSeq2SeqLM.from_pretrained(lora_base_path, torch_dtype=torch.bfloat16)
tokenizer = AutoTokenizer.from_pretrained(lora_model_path)
peft_model = PeftModel.from_pretrained(peft_model_base, 
                                       lora_model_path, 
                                       torch_dtype=torch.bfloat16,
                                       is_trainable=False)


def get_prompt(conv_log):
    INSTRUCTION = "### INSTRUCTION: \nGenerate summary of the below conversation\n\n"
    SAMPLE_RESPONSE = "### SUMMARY:\n"
    return f""" {INSTRUCTION} {conv_log}  {SAMPLE_RESPONSE}"""


def predict(conv_log):
    logger.info(f"trying to generate summary for {conv_log}")
    prompt = get_prompt(conv_log)
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    raw_output = peft_model.generate(input_ids=input_ids, generation_config=GenerationConfig(max_new_tokens=2000))
    output = tokenizer.decode(raw_output[0])
    with open("output.txt", "w") as f:
        f.write(str(output))
    temp = output.split("### SUMMARY")
    logger.info(f"len of temp : {len(temp)}")
    if len(temp) > 1:
        output = temp[-1]
    return output