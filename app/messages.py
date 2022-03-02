from flask import jsonify

DEFAULT_HEADERS = {"Content-Type": "application/json"}


def make_response(payload="", code=200):
    return (jsonify(payload), code, DEFAULT_HEADERS)


def not_authorized_error():
    return error("Not authorized", code=401)


def error(error_code_str, message_str=None, code=500):
    payload = {"errorCode": error_code_str}
    if message_str:
        payload["message"] = message_str

    return make_response(payload, code)

def not_found():
    return error("Not found", code=404)

def internal_error():
    return error("An internal error occurred", code=500)
