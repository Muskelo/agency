from datetime import datetime

from flaskr.db import db
from flaskr.mixins import BaseMixin, ImageMixin, ItemMixin, OrderMixin, UserMixin
from flaskr.utils import generate_symlink_on_id


class ImageModel(db.Model, ImageMixin):
    __tablename__ = 'image'

    # db data
    id = db.Column(db.Integer,  primary_key=True)
    filename = db.Column(db.String(255), unique=True)
    # Foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))

    @property
    def owner_id(self):
        return self.user_id


class OrderModel(db.Model, OrderMixin):
    __tablename__ = "order"

    # db data
    id = db.Column(db.Integer,  primary_key=True)
    created = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.String(255))
    comment = db.Column(db.Text)
    # Foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))

    
    @property
    def owner_id(self):
        return self.item.owner_id


class UserModel(db.Model, UserMixin):
    __tablename__ = 'user'

    # db data
    id = db.Column(db.Integer,  primary_key=True)
    login = db.Column(db.String(255), unique=True)
    number = db.Column(db.String(255), unique=True)
    role = db.Column(db.String(255))

    password_hash = db.Column(db.String(255))

    # relationships
    images = db.relationship(
        "ImageModel",  backref=db.backref("user"))
    orders = db.relationship(
        "OrderModel", cascade="delete, all",  backref=db.backref("user"))
    items_ = db.relationship(
        "ItemModel",  backref=db.backref("user"))

    @property
    def owner_id(self):
        return self.id

    @property
    def is_auth(self):
        return True


class ItemModel(db.Model, ItemMixin):
    __tablename__ = "item"

    # db data
    id = db.Column(db.Integer,  primary_key=True)
    size = db.Column(db.Integer)
    price = db.Column(db.BigInteger)
    rooms = db.Column(db.Integer)
    floor = db.Column(db.Integer)
    total_floor = db.Column(db.Integer)
    type = db.Column(db.String(255))
    city = db.Column(db.String(255))
    address = db.Column(db.Text)
    description = db.Column(db.Text)

    # foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    images_id = generate_symlink_on_id("images", ImageModel)

    # relationships
    images = db.relationship(
        "ImageModel",  backref=db.backref("item"))
    orders = db.relationship(
        "OrderModel", cascade="delete, all", backref=db.backref("item"))

    # cascade
    cascade_delete = ["images"]

    @property
    def owner_id(self):
        return self.user_id
