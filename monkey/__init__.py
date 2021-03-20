import logging
from flask import Flask

from . import db
from .graphql import gql_bp

logging.basicConfig(level=logging.DEBUG)


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = b'secret monkey'
    app.register_blueprint(gql_bp)

    db.connect_monkey(app.debug)
    db.insert_data_for_query()

    return app
