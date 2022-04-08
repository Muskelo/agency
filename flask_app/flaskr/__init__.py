from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from flaskr.db import db 
from flaskr.config import Configuration
from flaskr.resources import RoleResource, UserResource
from flaskr.default import init_default_data

def init_db(app):
    """ Init db and migrations. """

    db.init_app(app)
    Migrate(app, db)

def init_api(app):
    api = Api(app, prefix="/api")

    api.add_resource(UserResource, '/users/', '/users/<id>')
    api.add_resource(RoleResource, '/roles/', '/roles/<id>')


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)

    app.before_first_request(init_default_data)

    init_db(app)
    init_api(app)


    
    return app

