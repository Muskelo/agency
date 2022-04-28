from flask import g, request
from flask_restful import Resource, abort

from flaskr.models import RoleModel, UserModel, ImageModel
from flaskr.data_models import *
from flaskr.utils import with_data
from flaskr.auth import auth


class UserResource(Resource):
    @auth.login_required()
    def get_me(self):
        return auth.current_user()

    def get(self, id=None):
        if id:
            if int(id) != -1:
                user = UserModel.get_(id=id)

            # get current_user
            else:
                user = self.get_me()

            response_data = DumpUser(user=user).dict()

        else:
            users = UserModel.get_all_()
            response_data = DumpUsers(users=users).dict()

        return response_data

    @with_data(LoadUser)
    def post(self):
        user = UserModel.create_(**g.request_data['user'])

        return DumpUser(user=user).dict()

    @auth.login_required(role=['admin'], get_item_f=UserModel.get_)
    def delete(self, id):
        user = UserModel.delete_(id)

        return DumpUser(user=user).dict()

    @auth.login_required(role=['admin'], get_item_f=UserModel.get_)
    @with_data(LoadOptionalUser)
    def patch(self, id):
        user = UserModel.update_(id, **g.request_data['user'])

        return DumpUser(user=user).dict()


class RoleResource(Resource):
    @auth.login_required(role=['admin'])
    def get(self, id=None):
        if id:
            role = RoleModel.get_(id=id)
            response_data = DumpRole(role=role).dict()

        else:
            roles = RoleModel.get_all_()
            response_data = DumpRoles(roles=roles).dict()

        return response_data

    @auth.login_required(role=['admin'])
    @with_data(LoadOptionalRole)
    def patch(self, id):
        role = RoleModel.update_(id, **g.request_data['role'])

        return DumpRole(role=role).dict()


class ImageResource(Resource):

    @auth.login_required
    def post(self):
        image_file = request.files['image']

        image = ImageModel.create_(image_file=image_file, user_id=auth.current_user().id)

        return DumpImage(image=image).dict()

    def delete(self, id):
        image = ImageModel.delete_(id)

        return {"name": image["filename"]}
