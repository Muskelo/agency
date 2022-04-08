from flaskr.db import db
from flaskr.mixins import BaseMixin, UserMixin, generate_symlink_on_id

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
    users_id = generate_symlink_on_id("users", UserModel)

