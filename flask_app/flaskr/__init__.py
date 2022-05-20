from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from flaskr.db import db
from flaskr.config import Configuration
from flaskr.default import init_default_data
from flaskr.errors import init_error_handler
from flaskr.auth import auth
from flaskr.resources import (
    ImagesListResource, ImageResource,
    UserResource, UsersListResource,
    ItemResource, ItemsListResource,
    OrderResource, OrdersListResource)


def init_db(app):
    """ Init db and migrations. """

    db.init_app(app)
    Migrate(app, db)


def init_api(app):
    api = Api(app, prefix="/api")

    api.add_resource(ImageResource, '/image/<id>')
    api.add_resource(ImagesListResource, '/images/')

    api.add_resource(UserResource, '/user/<id>')
    api.add_resource(UsersListResource, '/users/')

    api.add_resource(ItemResource, '/item/<id>')
    api.add_resource(ItemsListResource, '/items/')

    api.add_resource(OrderResource, '/order/<id>')
    api.add_resource(OrdersListResource, '/orders/')


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)

    app.before_first_request(init_default_data)

    init_db(app)
    init_api(app)
    init_error_handler(app)

    @app.before_request
    def before_request():
        auth.set_current_user()

    return app
