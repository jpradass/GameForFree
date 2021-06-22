from flask_restful import Resource
from ..version import version

class Health(Resource):
    def get(self):
        return {'Status': 'OK'}, 200

class Version(Resource):
    def get(self):
        return {'Version': f'v{version}'}, 200

class Refresh(Resource):
    def put(self):
        return {}, 202