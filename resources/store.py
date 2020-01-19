from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {'message': 'Store does not exist'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'Store already exists'}, 400

        store = StoreModel(name=name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error has occured'}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            try:
                store.delete_from_db()
            except:
                {'message': 'An error has occured'}, 500

        return {'message': 'Store deleted'}

class StoreList(Resource):
    def get(self):
        return {'store': [store.json() for store in StoreModel.query.all()]}