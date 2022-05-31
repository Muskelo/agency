from base64 import b64decode
from functools import wraps

from flask import request, g
from flask_restful import abort
from passlib.hash import pbkdf2_sha256

from flaskr.models import UserModel


class Anonym():
    @property
    def is_auth(self):
        return False

    @property
    def role(self):
        return None


class Authorization():
    def login(self, login, password):
        user = UserModel.get_(False, login=login)

        print(user, flush=True)
        print(password, flush=True)

        if user and pbkdf2_sha256.verify(password, user.password_hash):
            return user
        else:
            abort(401, message="Invalida credentials.")

    def set_current_user(self):
        if request.headers.get("Authorization"):
            auth_string = request.headers.get("Authorization").split(" ")[1]
            login, password = b64decode(auth_string).decode('ascii').split(":")

            user = self.login(login, password)
        else:
            user = Anonym()

        g.current_user = user

    def check_role(self, roles):
        if not roles:
            return False

        if g.current_user.role in roles:
            return True

    def check_owner(self, get_f=None, view_arg="id", query_arg=None):
        if not get_f:
            return False

        if query_arg:
            id = request.args.get(query_arg)
        else:
            id = request.view_args[view_arg]

        item = get_f(id=id)

        return item.owner_id == g.current_user.id

    def auth_required(self, roles=None, owner=None):
        if not owner:
            owner = {}

        def decorator(f):
            @ wraps(f)
            def wrapper(*args, **kwargs):
                if not g.current_user.is_auth:
                    abort(401, message="Login required.")
                if roles or owner:
                    if not (self.check_role(roles) or self.check_owner(**owner)):
                        abort(403, message="You don't have permission")
                return f(*args, **kwargs)
            return wrapper
        return decorator


auth = Authorization()
