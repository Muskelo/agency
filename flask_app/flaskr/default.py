from flaskr.models import RoleModel, UserModel

def init_default_data():
    # definition admin role
    admin_role = RoleModel.get_(False, name="admin")
    if not admin_role:
        admin_role = RoleModel.create_(name="admin")

    # definition moder role
    moder_role = RoleModel.get_(False, name="moder")
    if not  moder_role:
        moder_role = RoleModel.create_(name="moder")

    # definition admir user
    admin_user = UserModel.get_(False, login="admin")
    if not  admin_user:
        admin_user = UserModel.create_(login="admin", email="admin@test.ru", password="admin")

    # set roles for admin user
    if not admin_user in admin_role.users:
        admin_role.users.append(admin_user)
    if not admin_user in moder_role.users:
        moder_role.users.append(admin_user)



