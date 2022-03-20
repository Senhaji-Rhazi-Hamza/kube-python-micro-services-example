import os
import config
import datetime

from flask import Flask, request

from app.lib.arithmetic import my_mul, my_sum
from app.messages import make_response

app = Flask(__name__)

@app.route('/', methods=["GET"])
def health_check():
    payload = {
                "message": "welcome to the example service ari - mul",
                "status": "success"
            }
    return make_response.message(payload, 200)


@app.route('/mul', methods=["POST"])
def mul():
    #import ipdb; ipdb.set_trace()
    l = request.get_json()['list']
    payload = {
        "message": "my mul function",
        "status": "success",
        "result" : my_mul(*l) * 2,
    }
    return make_response.message(payload)



if __name__ == "__main__":
    app.run(
        debug=config.DEBUG_MODE, host="0.0.0.0", port=os.getenv('PORT', 8001)
        )
