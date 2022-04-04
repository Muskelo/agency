from flaskr.db import db
from flaskr.mixins import UserMixin

class UserModel(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer,  primary_key=True)
    login = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
