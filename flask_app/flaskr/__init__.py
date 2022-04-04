from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from flaskr.db import db 
from flaskr.config import Configuration
from flaskr.resources import UserResource

def init_db(app):
    """ Init db and migrations. """

    db.init_app(app)
    Migrate(app, db)

def init_api(app):
    api = Api(app)

    api.add_resource(UserResource, '/users/', '/users/<user_id>')

def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)

    init_db(app)
    init_api(app)
    
    return app

