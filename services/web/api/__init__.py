from flask import (
    Flask
)
from api.extensions import (
    db,
    ma,
    migrate,
    bcrypt,
    jwt
)
from flask_restful import Api

from utils.errors import errors
from api.routes import load_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object("api.config.Config")
    app = register_plugins(app)
    return app


def register_plugins(app):
    db.init_app(app)
    route = Api(app, errors=errors, prefix="/api/v1")
    ma.init_app(app)
    migrate.init_app(app, db)

    # mail.init_app(app)

    bcrypt.init_app(app)
    jwt.init_app(app)
    load_routes(route)
    return app


app = create_app()
