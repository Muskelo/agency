from flaskr.models import UserModel


def init_default_data():
    # definition admir user
    admin_user = UserModel.get_(False, login="admin")
    if not admin_user:
        admin_user = UserModel.create_(
            login="admin", number="11111111111", password="admin", role="admin")

    # definition moder user
    moder_user = UserModel.get_(False, login="moder")
    if not moder_user:
        moder_user = UserModel.create_(
            login="moder", number="22222222222", password="moder", role="moder")

    # definition simple user
    moder_user = UserModel.get_(False, login="user")
    if not moder_user:
        moder_user = UserModel.create_(
            login="user", number="3333333333333", password="user")
