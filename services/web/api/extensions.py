from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail


db = SQLAlchemy()

ma = Marshmallow()
migrate = Migrate()

mail = Mail()

bcrypt = Bcrypt()
jwt = JWTManager()
