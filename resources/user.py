import sqlite3
from flask_restful import Resource, Api, reqparse
from models.user import UserModel
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token

class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username',
                            type=str,
                            required=True,
                            help='username is mandatory')

        parser.add_argument('password',
                            type=str,
                            required=True,
                            help='password is mandatory')

        data = parser.parse_args()

        user = UserModel.find_by_user_name(data['username'])

        if user:
            return {'message': 'user is already registered'}, 400




        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        #
        #
        # sql_insert_uset = 'INSERT INTO USERS VALUES(NULL,?,?)'

        # values = (data['username'],data['password'])

        # cursor.execute(sql_insert_uset, values)
        # connection.commit()
        # connection.close()

        user = UserModel(data['username'], data['password'])

        user.save_to_db()


        return {'message': 'User has been created'}


class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_user_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        return user.json()

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_user_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        user.delete_from_db()
        return {'message': 'User deleted'}, 200

class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='username is mandatory')

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='password is mandatory')
    @classmethod
    def post(cls):
        # get data from parser
        data = cls.parser.parse_args()
        # find user in DB
        user = UserModel.find_by_user_name(data.get('username'))
        # check passwords
        if user and safe_str_cmp(user.password, data.get('password')):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        return {'message': 'Invalid credential'}, 401
        # create access token
        # create refresh  token





