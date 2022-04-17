import os


from flask import Flask, request

from app.lib.arithmetic import my_sum
from app.messages import make_response
from app import config


app = Flask(__name__)

@app.route('/', methods=["GET"])
def health_check():
    payload = {
                "message": "welcome to the example microservice sum",
                "status": "success"
            }
    return make_response(payload, 200)


@app.route('/sum', methods=["POST"])
def sum():
    l = request.get_json()['list']
    
    payload = {
        "message": "my sum function from microservice",
        "status": "success",
        "result" : my_sum(*l),
    }
    return make_response(payload)




if __name__ == "__main__":
    app.run(
        debug=config.DEBUG_MODE, host="0.0.0.0", port=os.getenv('PORT', config.SUM_PORT)
        )
