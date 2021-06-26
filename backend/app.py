from ariadne.graphql import graphql_sync
from flask import Flask, request
# from flask_restful import Api
from ariadne import ObjectType, load_schema_from_path, make_executable_schema, snake_case_fallback_resolvers
from ariadne.constants import PLAYGROUND_HTML

import os

from flask.json import jsonify
from .db import db
from .resources.queries import resolve_games, resolve_game
from .resources.management import health, refresh, server_version

# from db import db
# from resources.management import health, refresh, server_version
# from resources.queries import resolve_games, resolve_game

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

query = ObjectType("Query")

query.set_field("games", resolve_games)
query.set_field("game", resolve_game)
type_defs = load_schema_from_path("backend/schemas/schema.graphql")
# type_defs = load_schema_from_path("schemas/schema.graphql")
schema = make_executable_schema(type_defs, query, snake_case_fallback_resolvers)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code

@app.route("/health", methods=["GET"])
def server_health():
    return jsonify(health()), 200

@app.route("/version", methods=["GET"])
def server_v():
    return jsonify(server_version()), 200

@app.route("/refresh", methods=["PUT"])
def refresh_games():
    return jsonify({"Games list refreshed?", refresh()}), 200

if __name__ == "__main__":

    db.init_app(app)
    app.run(port=5000, debug=True)