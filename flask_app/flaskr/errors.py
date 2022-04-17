from pydantic import ValidationError
from flask_restful import abort
from sqlalchemy.exc import IntegrityError

def init_error_handler(app):

    @app.errorhandler(ValidationError)
    def handle_validation_exception(e):
        abort(400, errors=e.errors())

    @app.errorhandler(IntegrityError)
    def handle_integrity_exception(e):
        abort(400, errors=e.orig.args)
