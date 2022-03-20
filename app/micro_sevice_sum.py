import os
import config
import datetime

from flask import Flask, request

from app.lib.arithmetic import my_sum, my_mul
from app.messages import make_response


app = Flask(__name__)

@app.route('/', methods=["GET"])
def health_check():
    payload = {
                "message": "welcome to the example service ari - sum",
                "status": "success"
            }
    return make_response.message(payload, 200)


@app.route('/sum', methods=["POST"])
def sum():
    l = request.get_json()['list']
    
    payload = {
        "message": "my sum function",
        "status": "success",
        "result" : my_sum(*l),
    }
    return make_response.message(payload)




if __name__ == "__main__":
    app.run(
        debug=config.DEBUG_MODE, host="0.0.0.0", port=os.getenv('PORT', 8002)
        )
