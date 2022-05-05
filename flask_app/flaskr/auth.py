from flask import request, g
from flask_httpauth import HTTPBasicAuth
from functools import wraps
from flask_restful import abort
from passlib.hash import pbkdf2_sha256

from flaskr.models import UserModel


class MyHTTPBasicAuth(HTTPBasicAuth):
    def login_required(self, f=None, role=None, optional=None, get_item_f=None, view_arg_name="id"):

        if f is not None and \
                (role is not None or optional is not None):  # pragma: no cover
            raise ValueError(
                'role and optional are the only supported arguments')

        def check_owner(user):
            if get_item_f:
                item_id = request.view_args[view_arg_name]
                item = get_item_f(id=item_id)

                if item.owner_id != user.id:
                    return False
            return True

        def login_required_internal(f):
            @wraps(f)
            def decorated(*args, **kwargs):
                auth = self.get_auth()

                # Flask normally handles OPTIONS requests on its own, but in
                # the case it is configured to forward those to the
                # application, we need to ignore authentication headers and
                # let the request through to avoid unwanted interactions with
                # CORS.
                if request.method != 'OPTIONS':  # pragma: no cover
                    password = self.get_auth_password(auth)

                    status = None
                    user = self.authenticate(auth, password)
                    if user in (False, None):
                        status = 401
                    elif not (check_owner(user) or self.authorize(role, user, auth)):
                        status = 403
                    if not optional and status:
                        try:
                            return self.auth_error_callback(status)
                        except TypeError:
                            return self.auth_error_callback()

                    g.flask_httpauth_user = user if user is not True \
                        else auth.username if auth else None
                return self.ensure_sync(f)(*args, **kwargs)
            return decorated

        if f:
            return login_required_internal(f)
        return login_required_internal


auth = MyHTTPBasicAuth()


@auth.get_user_roles
def get_user_roles(user):
    return [user.role]

@auth.verify_password
def verify_password(username, password):
    user = UserModel.get_(False, login=username)

    if user and pbkdf2_sha256.verify(password, user.password_hash):
        return user

@auth.error_handler
def auth_error(status):
    return abort(status)
