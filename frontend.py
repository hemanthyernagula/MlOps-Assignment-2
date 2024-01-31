import gradio as gr
from loguru import logger
import requests

def get_predictions(file_path):

    url = "http://localhost:8080/predict"

    payload = {}
    files=[
    ('file',('test.json',open(file_path,'rb'),'application/json'))
    ]
    headers = {}
    logger.info(f"hitting model api")
    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response.text

def zip_to_json(file_obj):
    files = []
    output = get_predictions(file_obj)
    return output


demo = gr.Interface(zip_to_json, "file", "json")

if __name__ == "__main__":
    demo.launch()