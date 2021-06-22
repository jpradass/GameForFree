from flask_restful import Resource

class Health(Resource):
    def get(self):
        return {'Status': 'OK'}, 200

class Refresh(Resource):
    def put(self):
        return {}, 202