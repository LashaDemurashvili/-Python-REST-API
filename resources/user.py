from flask_restful import Resource, reqparse, marshal_with, fields
from models.user import UserModel
from flask_jwt_extended import jwt_required

User_fields = {
    "id": fields.Integer,
    "username": fields.String,
    "password": fields.String
}

class UserResource(Resource):
    my_parser = reqparse.RequestParser()

    my_parser.add_argument('username',
                           type=str,
                           required=True,
                           help="Username is required!")
    my_parser.add_argument('password',
                           type=str,
                           required=True,
                           help="Password is required!")


    @marshal_with(User_fields)
    # @jwt_required()
    def get(self, id=None):
        if id:
            return UserModel.query.get(id)
        return UserModel.query.all()

    @jwt_required()
    def delete(self, username):
        item = UserModel.find_by_username(username)
        if item:
            item.delete_item_from_db()
            return {"message": "User was successfully deleted"}, 200
        return {"message": "User not found"}
