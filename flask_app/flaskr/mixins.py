import os

from flask import current_app, request, g
from flask_restful import abort
from passlib.hash import pbkdf2_sha256
from werkzeug.utils import secure_filename

from flaskr.utils import save_in_db


class BaseMixin():
    """ Base Mixin

    include methods to work with SQLAlchemy models """

    @classmethod
    def get_(cls, with_abort: bool = True, **kwargs):
        item = cls.query.filter_by(**kwargs).first()

        if with_abort and not item:
            abort(404)

        return item

    @classmethod
    def get_list_(cls, default_limit=20, filter_=None,  filter_by=None):
        query = cls.query

        # filter
        if filter_by:
            query = query.filter_by(**filter_by)

        if filter_:
            for key, value in filter_.items():
                query = query.filter(getattr(cls, key) == value)

        # total, offset,limit
        total = query.count()
        offset = request.args.get("offset")

        if offset:
            query = query.offset(offset)

        limit = request.args.get("limit") or default_limit
        query = query.limit(limit)

        return query.all(), total

    @classmethod
    def create_(cls, **kwargs):
        item = cls(**kwargs)

        save_in_db(add=[item])

        return item

    @classmethod
    def delete_(cls, id):
        item = cls.get_(id=id)

        # cascade deleting
        if hasattr(item, "cascade_delete"):
            for relationship in item.cascade_delete:
                map(lambda item: item.delete_(item.id),
                    getattr(item, relationship))

        save_in_db(delete=[item])

        return item

    @classmethod
    def update_(cls, id, **kwargs):
        item = cls.get_(id=id)

        for key, value in kwargs.items():
            if value:
                setattr(item, key, value)

        save_in_db()

        return item


class OrderMixin(BaseMixin):
    @classmethod
    def get_list_(cls, default_limit=20, filter_=None,  filter_by=None, ItemModel=None, UserModel=None):
        query = cls.query.join(cls.item).join(ItemModel.user)

        # filter
        if filter_by:
            query = query.filter_by(**filter_by)

        if filter_:
            for key, value in filter_.items():
                query = query.filter(getattr(cls, key) == value)

        query = query.filter(UserModel.id == g.current_user.id)

        # total, offset,limit
        total = query.count()
        offset = request.args.get("offset")

        if offset:
            query = query.offset(offset)

        limit = request.args.get("limit") or default_limit
        query = query.limit(limit)

        return query.all(), total


class UserMixin(BaseMixin):
    """ User Mixin """

    @classmethod
    def create_(cls, **kwargs):

        print(kwargs, flush=True)

        kwargs["password_hash"] = pbkdf2_sha256.hash(kwargs['password'])
        kwargs.pop("password")

        print(kwargs, flush=True)

        user = super().create_(**kwargs)

        return user

    @classmethod
    def update_(cls, id, **kwargs):
        if "password" in kwargs:
            kwargs["password_hash"] = pbkdf2_sha256.hash(kwargs['password'])
            kwargs.pop("password")

        user = super().update_(id, **kwargs)

        return user


class ImageMixin(BaseMixin):
    @staticmethod
    def save_image(image_file, image_id):
        image_filename = secure_filename(image_file.filename)
        new_filename = os.path.join(
            current_app.config['UPLOAD_FOLDER'], f"{image_id}__{image_filename}")

        try:
            image_file.save(new_filename)
        except:
            super().delete_(image_id)
            abort(500)

        return new_filename

    @classmethod
    def create_(cls, image_file, **kwargs):

        # create image object in DB
        image = super().create_(**kwargs)

        new_filename = cls.save_image(image_file, image.id)

        # update filename if file saved
        image = super().update_(image.id, filename=new_filename)

        return image


class ItemMixin(BaseMixin):
    @classmethod
    def get_list_(cls, default_limit=20, filter_by=None, min_price=None, max_price=None):
        query = cls.query

        # filter
        if filter_by:
            query = query.filter_by(**filter_by)

        if min_price:
            query = query.filter(cls.price > min_price)
        if max_price:
            query = query.filter(cls.price < max_price)

        total = query.count()

        # offset,limit
        offset = request.args.get("offset")
        if offset:
            query = query.offset(offset)

        limit = request.args.get("limit") or default_limit
        query = query.limit(limit)

        return query.all(), total
