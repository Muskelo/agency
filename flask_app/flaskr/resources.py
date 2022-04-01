from flask_restful import Resource
from models import UserModel

class UserResource(Resource):
    def get(self):
        users = UserModel.get_all_()
        return {'hello': 'world'}
