import os
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
#from security import authenticate, identity
from resources.item import Item, ItemList
from resources.user import UserRegister, User, UserLogin
from resources.store import Store, StoreList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['PROPAGATE_EXCEPTIONS'] = True

app.secret_key = 'pass'

api = Api(app)


#jwt = JWT(app, authenticate, identity)
jwt =JWTManager(app)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/registration')
api.add_resource(Store,  '/store/<string:name>')
api.add_resource(StoreList,  '/stores')
api.add_resource(User,  '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')



if __name__ == '__main__':

    from db import db

    db.init_app(app)
    app.run(port=6000, debug=True)
