import os
import config
import datetime

from flask import Flask, request

#from lib.arithmetic import my_sum, my_mul
from messages import make_response
from app import messages

app = Flask(__name__)

# @app.route('/', methods=["GET"])
# def health_check():
#     payload = {
#                 "message": "welcome to the example service",
#                 "status": "success"
#             }
#     return make_response.message(payload, 200)


# @app.route('/sum', methods=["POST"])
# def sum():
#     l = request.get_json()['list']
    
#     payload = {
#         "message": "my sum function",
#         "status": "success",
#         "result" : my_sum(*l),
#     }
#     return make_response.message(payload)


# @app.route('/mul', methods=["POST"])
# def mul():
#     l = request.get_json()['list']
#     payload = {
#         "message": "my mul function",
#         "status": "success",
#         "result" : my_mul(*l),
#     }
#     return make_response.message(payload)



if __name__ == "__main__":
    app.run(
        debug=config.DEBUG_MODE, host="0.0.0.0", port=os.getenv('PORT', 8000)
        )
