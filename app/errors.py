from app.config import logging
from app import messages


def setup(app):
    app.register_error_handler(Exception, error_handler)
    app.register_error_handler(404, not_found)


def error_handler(e):
    logging.exception("An error occurred during a request.")
    logging.exception(e)

    return messages.internal_error()

def not_found(e):
    logging.exception(e)
    return messages.not_found()