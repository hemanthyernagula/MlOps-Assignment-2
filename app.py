from flask import Flask, request
from model_inferance import predict as get_summary
import json

app = Flask(__name__)

@app.route("/livecheck")
def livecheck():
    return {
        "status": "ok"
    }

@app.route("/predict", methods=["POST"])
def predict():
    try:
        file = request.files['file']
        data = json.loads(file.read())
        dialouge = data.get("dialouge")
        output = get_summary(dialouge)
    except Exception as err:
        return {
            "status" : f"please check the file :err: {err}"
        }
    else:
        return {
            "status": "ok",
            "summary": output
        }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)