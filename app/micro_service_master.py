import os

import requests
from flask import Flask, request

from app.messages import make_response
from app import config


app = Flask(__name__)

@app.route('/', methods=["GET"])
def health_check():
    payload = {
                "message": "welcome to the service ari-entry",
                "status": "success"
            }
    return make_response.message(payload, 200)


@app.route('/sum', methods=["POST"])
def sum():
    l = request.get_json()['list']
    payload = {
            "list": l
    }
    response = requests.post(f'http://{config.SUM_HOST}:8002/sum', json=payload)
    return make_response.message(response.json())


@app.route('/mul', methods=["POST"])
def mul():
    l = request.get_json()['list']
    payload = {
            "list": l
    }
    response = requests.post(f'http://{config.MUL_HOST}:8001/mul', json=payload)
    return make_response.message(response.json())



if __name__ == "__main__":
    app.run(
        debug=config.DEBUG_MODE, host="0.0.0.0", port=os.getenv('PORT', 8000)
        )
