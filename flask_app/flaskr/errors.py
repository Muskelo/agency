from pydantic import ValidationError
from flask_restful import abort

def init_error_handler(app):

    @app.errorhandler(ValidationError)
    def handle_exception(e):
        abort(400, vaidation_errors=e.errors())
