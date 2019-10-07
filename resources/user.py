import sqlite3
from flask_restful import Resource, Api, reqparse
from models.user import UserModel


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




