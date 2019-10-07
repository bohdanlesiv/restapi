from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.get_store_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        store = StoreModel.get_store_by_name(name)
        if store:
            return {'message': 'Store {} is present'.format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return  {'message': 'Error during store creation '.format(name)}, 500

        return store.json(), 201


    def delete(self, name):
        store = StoreModel.get_store_by_name(name)

        if store:
            store.delete_from_db()

        return {'message': 'Store {} has been  deleted'.format(name)}

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}

