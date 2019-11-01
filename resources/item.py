from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required
from flask import request
from models.item import ItemModel
import sqlite3



class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='price is mandatory')

    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='store is mandatory')


    @jwt_required
    def get(self, name):
        # item = next(filter(lambda item:  item['name'] == name ,items),None)
        item = ItemModel.get_item_by_name(name)

        if item:
            return item.json()

        return {'message': 'Item not found'}, 404



    def post(self, name):
        if ItemModel.get_item_by_name(name):
            return {'message': 'item {} is present'.format(name)}, 400

        data = Item.parser.parse_args()
        price = data['price']
        store_id = data['store_id']

        item = ItemModel(name=name, price=price, store_id=store_id)

        #){'price': price, 'name': name}

        try:
            item.save_to_db()
        except:
            return {'message': 'insert item error'}, 500
        return item.json(), 201


    def delete(self,name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # sql_delete_query = 'DELETE from ITEMS where ITEM = ?'
        # cursor.execute(sql_delete_query, (name,))
        # connection.commit()
        # connection.close()

        item = ItemModel.get_item_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'item {} has been deleted'.format(name)}

    def put(self, name):

        data = Item.parser.parse_args()
        price = data['price']
        store_id = data['store_id']


        item = ItemModel.get_item_by_name(name)

        if item is None:
            item = ItemModel(name, price, store_id)
        else:
            item.price = price

        item.save_to_db()

        # return item.json()


class ItemList(Resource):
    def get(self):
        # return {'items': [item.json() for item in ItemModel.query.all()]}
        return {'items': [item.json() for item in ItemModel.find_all()]}
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # sql_get_all = 'SELECT * FROM  ITEMS'
        # result = cursor.execute(sql_get_all)
        # rows = result.fetchall()

        # items = []

        # for row in rows:
        #     items.append({'name': row[0], 'price': row[1]})

        # return {'items': items}


