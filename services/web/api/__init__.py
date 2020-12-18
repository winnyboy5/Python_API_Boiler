import os

from werkzeug.utils import secure_filename
from flask import (
    Flask
)
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail


from utils.errors import errors

app = Flask(__name__)
app.config.from_object("api.config.Config")

db = SQLAlchemy(app)
route = Api(app, errors=errors)
ma = Marshmallow(app)
migrate = Migrate(app, db)

mail = Mail(app)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)


from api import routes
