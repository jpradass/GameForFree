from flask import Flask
from flask_restful import Api

import os
from db import db
from resources.management import Health, Refresh

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
api = Api(app)

api.add_resource(Health, '/_health')
api.add_resource(Refresh, '/_refresh')

if __name__ == "__main__":

    db.init_app(app)
    app.run(port=5000, debug=True)