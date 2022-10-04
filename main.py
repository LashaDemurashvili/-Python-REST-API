from flask import Flask, redirect
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.register import Register
from resources.login import Login
from models import db
from resources import ItemResource, ItemList, UserResource

app = Flask(__name__)
api = Api(app)

app.config["JWT_SECRET_KEY"] = "Secret_Secret_Secret"
jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/")
def home():
    return "<h1> This is my API</h1>"

@app.route("/git")
def about():
    return redirect("https://github.com/LashaDemurashvili")



api.add_resource(Login, "/api/login")
api.add_resource(Register, "/api/register")

api.add_resource(ItemList, "/api/items")
api.add_resource(ItemResource, "/api/items/<string:name>", "/api/items")
api.add_resource(UserResource, "/api/user/<int:id>", "/api/user", "/api/user/<string:username>")


@app.before_first_request
def create_table():
    db.create_all()


if __name__ == '__main__':
    app.run(port=5000, debug=True)


