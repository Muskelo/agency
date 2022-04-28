from flaskr.db import db
from flaskr.mixins import BaseMixin, ImageMixin, UserMixin
from flaskr.utils import generate_symlink_on_id

user_role = db.Table('user_role',
                     db.Column('user_id', db.Integer, db.ForeignKey(
                         'user.id'), primary_key=True),
                     db.Column('role_id', db.Integer, db.ForeignKey(
                         'role.id'), primary_key=True)
                     )


class UserModel(UserMixin, db.Model):
    __tablename__ = 'user'

    # db data
    id = db.Column(db.Integer,  primary_key=True)
    login = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))

    # relationships
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

    # db data
    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(255))

    # relationships
    users_id = generate_symlink_on_id("users", UserModel)

class HousingModel(db.Model, BaseMixin):
    __tablename__ = "housing"

    # db data
    id = db.Column(db.Integer,  primary_key=True)
    rooms = db.Column(db.Integer)
    size = db.Column(db.Integer)
    floor = db.Column(db.Integer)
    floor_total = db.Column(db.Integer)
    city = db.Column(db.String(255))
    address = db.Column(db.Text)
    price = db.Column(db.BigInteger)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # relationships
    user = db.relationship("UserModel", backref = db.backref("housings"))

    @property
    def owner_id(self):
        return self.user_id

class ImageModel(db.Model, ImageMixin):
    __tablename__ = 'image'

    # db data
    id = db.Column(db.Integer,  primary_key=True)
    filename = db.Column(db.String(255), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    housing_id = db.Column(db.Integer, db.ForeignKey("housing.id"))

    # relationships
    user = db.relationship("UserModel", backref = db.backref("images", cascade="delete, all"))
    housing = db.relationship("HousingModel", backref = db.backref("images"))

    @property
    def owner_id(self):
        return self.user_id

