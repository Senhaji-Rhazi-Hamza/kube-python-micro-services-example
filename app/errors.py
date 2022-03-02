from app.config import logging
from app.messages import make_response


def setup(app):
    app.register_error_handler(Exception, error_handler)
    app.register_error_handler(404, not_found)


def error_handler(e):
    logging.exception("An error occurred during a request.")
    logging.exception(e)

    return make_response.internal_error()

def not_found(e):
    logging.exception(e)
    return make_response.not_found()