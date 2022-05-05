import os

from flask import current_app
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
    def get_all_(cls, **kwargs):
        items = cls.query.filter_by(**kwargs).all()

        return items

    @classmethod
    def create_(cls, **kwargs):
        item = cls(**kwargs)

        save_in_db(add=[item])

        return item

    @classmethod
    def delete_(cls, id):
        item = cls.get_(id=id)

        # cascade deleting
        if item.cascade_delete:
            for related_items in item.cascade_delete:
                map(lambda item: item.delete_(item.id), related_items)

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


class UserMixin(BaseMixin):
    """ User Mixin """

    @classmethod
    def create_(cls, **kwargs):
        kwargs["password_hash"] = pbkdf2_sha256.hash(kwargs['password'])
        kwargs.pop("password")

        user = super().create_(**kwargs)

        return user

    @classmethod
    def update_(cls, id, **kwargs):
        if kwargs["password"]:
            kwargs["password_hash"] = pbkdf2_sha256.hash(kwargs['password'])
            kwargs.pop("password")

        user = super().update_(id, **kwargs)

        return user


class ImageMixin(BaseMixin):
    @classmethod
    def create_(cls, **kwargs):

        # get image info
        image_file = kwargs.pop("image_file")
        image_filename = secure_filename(image_file.filename)

        # create image object in DB
        image = super().create_(**kwargs)

        # try save image file
        filename = os.path.join(
            current_app.config['UPLOAD_FOLDER'], f"{image.id}__{image_filename}")
        try:
            image_file.save(filename)
        except:
            super().delete_(image.id)
            abort(500)

        # update filename if file saved
        image = super().update_(image.id, filename=filename)

        return image
