from sqlalchemy.ext.declarative import synonym_for
from flaskr.db import db
from flaskr.mixins import BaseMixin, UserMixin

user_role = db.Table('user_role',
                     db.Column('user_id', db.Integer, db.ForeignKey(
                         'user.id'), primary_key=True),
                     db.Column('role_id', db.Integer, db.ForeignKey(
                         'role.id'), primary_key=True)
                     )


class UserModel(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer,  primary_key=True)
    login = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))

    roles = db.relationship('RoleModel', secondary=user_role, lazy='subquery',
                            backref=db.backref('users', lazy=True))

    @synonym_for("roles")
    @property
    def roles_id(self):
        return [role.id for role in self.roles]


    @property
    def owner_id(self):
        return self.id


class RoleModel(db.Model, BaseMixin):
    __tablename__ = 'role'

    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(255))

    @property
    def users_id(self):
        return [user.id for user in self.users]

    @users_id.setter
    def users_id(self, new_value):
        new_value = set(new_value)
        users_id = set(self.users_id)

        append_users_id = new_value.difference(users_id)

        if append_users_id:
            for user_id in append_users_id:
                user = UserModel.get_(id=user_id)
                self.users.append(user)

        pop_users_id = users_id.difference(new_value)

        if pop_users_id:
            for user_id in pop_users_id:
                user = UserModel.get_(id=user_id)
                self.users.append(user)



