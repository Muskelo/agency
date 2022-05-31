from flask import g, request
from flask_restful import Resource, abort

import flaskr.pydantic_models as pm
from flaskr.models import ItemModel, OrderModel, UserModel, ImageModel
from flaskr.utils import with_data
from flaskr.auth import auth


class UserResource(Resource):
    @auth.auth_required()
    def get_me(self):
        return g.current_user

    @auth.auth_required(roles=["admin"], owner={"get_f": UserModel.get_})
    def get_user(self, id):
        return UserModel.get_(id=id)

    def get(self, id):
        if int(id) != -1:
            user = self.get_user(id)

            return pm.DumpUser(data=user).dict()
        else:  # get current_user
            user = self.get_me()

            return pm.DumpCurrentUser(data=user).dict()

    @auth.auth_required(owner={"get_f": UserModel.get_})
    @with_data(pm.PatchUser)
    def patch(self, id):
        user = UserModel.update_(id, **g.request_body['data'])

        return pm.DumpUser(data=user).dict()


class UsersListResource(Resource):

    @auth.auth_required(roles=["admin"])
    def get(self):
        users, total = UserModel.get_list_()

        return pm.DumpUsersList(data=users, total=total).dict()

    @with_data(pm.CreateUser)
    def post(self):
        user = UserModel.create_(**g.request_body['data'], role="user")

        return pm.DumpUser(data=user).dict()


class ImageResource(Resource):
    def delete(self, id):
        image = ImageModel.delete_(id)

        return pm.DumpImage(data=image).dict()


class ImagesListResource(Resource):
    @auth.auth_required(roles=["admin", "moder"])
    def get(self):
        images, total = ImageModel.get_list_(
            filter_by={"user_id": g.current_user.id, "item_id": None}
        )

        return pm.DumpImagesList(data=images).dict()

    @auth.auth_required()
    def post(self):
        image_file = request.files['image']
        if not image_file:
            abort(400, message="Image required")

        item_id = request.args.get("item_id") or None

        image = ImageModel.create_(
            image_file, user_id=g.current_user.id, item_id=item_id)

        return pm.DumpImage(data=image).dict()


class ItemResource(Resource):
    def get(self, id):
        item = ItemModel.get_(id=id)

        return pm.DumpItem(data=item).dict()

    @auth.auth_required(roles=["admin"], owner={"get_f": ItemModel.get_})
    @with_data(pm.PatchItem)
    def patch(self, id):
        item = ItemModel.update_(id, **g.request_body['data'])

        return pm.DumpItem(data=item).dict()

    @auth.auth_required(roles=["admin"], owner={"get_f": ItemModel.get_})
    def delete(self, id):
        item = ItemModel.delete_(id)

        return pm.DumpItem(data=item).dict()


class ItemsListResource(Resource):
    def get(self):

        filter_keys = ["city", "type", "rooms"]
        filter_by = {key: request.args.get(key)
                     for key in filter_keys if request.args.get(key)}

        min_price = request.args.get("min_price")
        max_price = request.args.get("max_price")

        items, total = ItemModel.get_list_(
            filter_by=filter_by, min_price=min_price, max_price=max_price)

        return pm.DumpItemsList(data=items, total=total).dict()

    @auth.auth_required(roles=["admin", "moder"])
    @with_data(pm.CreateItem)
    def post(self):

        # user_id is set automatically
        if "user_id" in g.request_body['data']:
            del g.request_body['data']['user_id']

        item = ItemModel.create_(
            user_id=g.current_user.id, **g.request_body['data'])

        return pm.DumpItem(data=item).dict()


class OrderResource(Resource):
    @auth.auth_required(roles=["admin", "moder"])
    @with_data(pm.PatchOrder)
    def patch(self, id):
        order = OrderModel.update_(id, **g.request_body['data'])

        return pm.DumpOrder(data=order).dict()

    @auth.auth_required(roles=["admin", "moder"])
    def delete(self, id):
        OrderModel.delete_(id)

        return {}


class OrdersListResource(Resource):
    @auth.auth_required(roles=["admin", "moder"])
    def get(self):
        filter_keys = ["item_id"]
        filter_ = {key: request.args.get(key)
                   for key in filter_keys if request.args.get(key)}

        orders, total = OrderModel.get_list_(
            filter_=filter_, ItemModel=ItemModel, UserModel=UserModel)

        return pm.DumpOrdersList(data=orders, total=total).dict()

    @auth.auth_required()
    @with_data(pm.CreateOrder)
    def post(self):
        order = OrderModel.create_(
            **g.request_body['data'], user_id=g.current_user.id, status="Новая")

        return pm.DumpOrder(data=order).dict()
