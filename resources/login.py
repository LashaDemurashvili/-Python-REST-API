from flask import request, jsonify
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash

from models.user import UserModel

class Login(Resource):
    def post(self):
        username = request.json.get("username", None)
        password = request.json.get("password", None)

        user = UserModel.query.filter_by(username=username).first()
        if user is None:
            return {"message": "bad username"}, 401

        # log in with actually password
        ok = check_password_hash(user.password, password)
        if not ok:
            return {"message": "password didn't match"}

        # # log in with created token
        # if user.password != password:
        #     return {"message": "password didn't match"}

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
