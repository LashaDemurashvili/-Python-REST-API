from flask_restful import Resource
from werkzeug.security import generate_password_hash

from resources.user import UserResource
from models.user import UserModel
from models import db

class Register(Resource):
    def post(self):
        params = UserResource.my_parser.parse_args()

        password_hash = generate_password_hash(params.get('password'))

        if UserModel.find_by_username(params['username']):
            return {"message": "User with this username already exists."}, 400

        user = UserModel(username=params.get('username'), password=password_hash)
        db.session.add(user)
        db.session.commit()

        return {"status": "ok"}
