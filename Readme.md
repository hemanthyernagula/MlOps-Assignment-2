# Summarization Of Conversation Logs
## Approach:
    1. Prompt fine tuning with zero shot, one shot.
    2. Lora Fine Tuning and comparing the Bleu Score, Rouge Score.

## commands to run docker
    docker pull yernagulahemanth/summarize:v0.2

    docker run -itd --name sum --network=host --gpus all summarization:latest

## curl request
    curl --location 'localhost:8080/predict' --form 'file=@"/C:/Assignments/Uniphore/MlOps-Assignment-2/test.json"'

## Frontend
    UI can be assessed from Gradio default port
    > http://127.0.0.1:7860