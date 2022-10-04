# resource - ში კოდის ის ნაწილი რომელიც API - სთან მუშაოსბს
from flask_jwt_extended import jwt_required
from flask_restful import reqparse, Resource, fields
from models.item import ItemModels


Item_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "price": fields.Integer,
    "quantity": fields.Integer
}


class ItemList(Resource):
    # @jwt_required()
    def get(self):
        return {'List of all products': list(map(lambda item: item.json(), ItemModels.query.all()))}


class ItemResource(Resource):
    my_parser = reqparse.RequestParser()
    my_parser.add_argument('name', required=True, help='name must be unique')
    my_parser.add_argument('price', required=True, help='price must be integer')
    my_parser.add_argument('quantity', required=True, help='quantity may be integer or float')


    # @jwt_required()
    def get(self, name):
        item = ItemModels.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Product not found"}, 404


    @jwt_required()
    def post(self):
        params = ItemResource.my_parser.parse_args()
        if ItemModels.find_by_name(params['name']):
            return "This product already exist"
        else:
            item = ItemModels(params['name'], params['price'], params['quantity'])
        item.add_item_to_db()
        return {"status": "ok"}


    @jwt_required()
    def put(self, name):
        try:
            data = ItemResource.my_parser.parse_args()
            item = ItemModels.find_by_name(name)

            if item:
                item.name = data['name']
                item.price = data['price']
                item.quantity = data['quantity']
            else:
                item = ItemModels(data['name'], data['price'], data['quantity'])
            item.add_item_to_db()
            return item.json()
        except:
            return "Bad request : url - name and transferred name must be match!"


    @jwt_required()
    def delete(self, name):
        item = ItemModels.find_by_name(name)
        if item:
            item.delete_item_from_db()
            return {"message": "Product was successfully deleted"}, 200

        return {"message": "Product with this name was not found"}, 404


