from flask_restful import abort
from passlib.hash import pbkdf2_sha256

from flaskr.utils import save_in_db

class BaseMixin():
    """ Base Mixin

    include methods to work with SQLAlchemy models """

    @classmethod
    def get_(cls, with_abort: bool=False, **kwargs):
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

class UserMixin(BaseMixin):
    """ User Mixi """

    @classmethod
    def create_(cls, **kwargs):

        kwargs["password_hash"] = pbkdf2_sha256.hash(kwargs['password'])
        kwargs.pop("password")

        user = super().create_(**kwargs)

        return user
