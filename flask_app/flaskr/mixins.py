from flask_restful import abort
from passlib.hash import pbkdf2_sha256

from flaskr.utils import save_in_db


def generate_symlink_on_id(items_name, ItemModel):

    def get_items_id(self):
        return [item.id for item in getattr(self, items_name)]

    def set_items_id(self, new_value):
        new_value = set(new_value)
        items_id = set(get_items_id(self))
        items = getattr(self, items_name)

        append_items_id = new_value.difference(items_id)

        if append_items_id:
            for item_id in append_items_id:
                item = ItemModel.get_(id=item_id)
                items.append(item)

        pop_items_id = items_id.difference(new_value)

        if pop_items_id:
            for item_id in pop_items_id:
                item = ItemModel.get_(id=item_id)
                items.remove(item)

        setattr(self, items_name, items)

    return property(fget=get_items_id, fset=set_items_id)


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

