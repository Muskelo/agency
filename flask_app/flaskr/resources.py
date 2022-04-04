from flask import g
from flask_restful import Resource

from flaskr.models import UserModel
from flaskr.data_models import DumpUser, DumpUsers, LoadUser
from flaskr.utils import with_data


class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = UserModel.get_(True, id=user_id)
            response_data = DumpUser(user=user).dict()

        else:
            users = UserModel.get_all_()
            response_data = DumpUsers(users=users).dict()

        return response_data

    @with_data(LoadUser)
    def post(self):
        user = UserModel.create_(**g.request_data['user'])
        response_data = DumpUser(user=user)
        
        return response_data
        
