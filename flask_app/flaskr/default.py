from flaskr.models import RoleModel, UserModel

def init_default_data():
    if not RoleModel.get_(False, name="admin"):
        RoleModel.create_(name="admin")

    if not RoleModel.get_(False, name="moder"):
        RoleModel.create_(name="admin")

    if not UserModel.get_(False, login="admin"):
        UserModel.create_(login="admin", email="admin@test.ru", password="admin")

