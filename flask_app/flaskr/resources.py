from typing import List
from pydantic import BaseModel
from flask import current_app
from flask_restful import Resource

from flaskr.models import UserModel


class User(BaseModel):
    id: int
    login: str
    email: str
    password_hash: str

    class Config:
        orm_mode = True


class Users(BaseModel):
    users: List[User]


class UserResource(Resource):
    def get(self):
        # users = UserModel.get_all_()
        # # current_app.logger.info(users)

        # return {'users' : [User.from_orm(user).dict() for user in users]}
        users = Users(users=UserModel.get_all_())
        # current_app.logger.info(users)

        return {'users': users.dict()}
