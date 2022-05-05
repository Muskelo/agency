from flask import g, request
from flask_restful import Resource, abort

import flaskr.pydantic_models as pm
from flaskr.models import UserModel, ImageModel
from flaskr.data_models import *
from flaskr.utils import with_data
from flaskr.auth import auth


class UserResource(Resource):
    @auth.login_required()
    def get_me(self):
        return auth.current_user()

    @auth.login_required(role="admin", get_item_f=UserModel.get_)
    def get_user(self, id):
        return UserModel.get_(id=id)

    def get(self, id):
        if int(id) != -1:
            user = self.get_user(id)

        else:  # get current_user
            user = self.get_me()

        return pm.DumpUser(data=user).dict()


class UsersListResource(Resource):

    @with_data(pm.CreateUser)
    def post(self):
        user = UserModel.create_(**g.request_data['data'])

        return pm.DumpUser(data=user).dict()

    @auth.login_required(role=['admin'], get_item_f=UserModel.get_)
    def delete(self, id):
        user = UserModel.delete_(id)

        return DumpUser(data=user).dict()

    @auth.login_required(role=['admin'], get_item_f=UserModel.get_)
    @with_data(LoadOptionalUser)
    def patch(self, id):
        user = UserModel.update_(id, **g.request_data['user'])

        return DumpUser(user=user).dict()


class ImageResource(Resource):

    @auth.login_required
    def post(self):
        image_file = request.files['image']

        image = ImageModel.create_(
            image_file=image_file, user_id=auth.current_user().id)

        return DumpImage(image=image).dict()

    def delete(self, id):
        image = ImageModel.delete_(id)

        return {"name": image["filename"]}
