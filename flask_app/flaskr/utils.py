from flask import request, g
from sqlalchemy.exc import SQLAlchemyError

from flaskr.db import db

def save_in_db(add: dict=[], delete: dict=[]) -> None: 
    """ Try save changes in db,
    add: itrable list on objects to save in db
    delete: itrable list on objects to delete from db
    """
    try:
        for item in add:
            db.session.add(item)

        for item in delete:
            db.session.delete(item)

        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e

def with_data(LoadClass=None):
    """ with_data,
    execute func with json data from request,

    LoadClass: validate data with pydantic model
    """
    def decorator(f):
        def wrapped(*args, **kwargs):
            # get data
            data = request.get_json()

            if LoadClass:
                data = LoadClass(**data).dict()

            g.request_data = data

            # execute f
            result = f(*args, **kwargs)

            # clean
            del g.request_data

            return result
        return wrapped
    return decorator
