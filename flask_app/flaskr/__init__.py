from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from flaskr.db import db
from flaskr.config import Configuration
from flaskr.resources import ImageResource, UserResource, UsersListResource
from flaskr.default import init_default_data
from flaskr.errors import init_error_handler


def init_db(app):
    """ Init db and migrations. """

    db.init_app(app)
    Migrate(app, db)


def init_api(app):
    api = Api(app, prefix="/api")

    api.add_resource(UserResource, '/user/<id>')
    api.add_resource(UsersListResource, '/users/')
    api.add_resource(ImageResource, '/images/', '/roles/<id>')


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)

    app.before_first_request(init_default_data)

    init_db(app)
    init_api(app)
    init_error_handler(app)

    return app
