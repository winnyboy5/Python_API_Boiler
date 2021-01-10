import os
from utils.converters import str_to_bool

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/api/static/"
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/api/media/"
    SECRET_KEY = os.getenv("SECRET_KEY")
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_USE_TLS = str_to_bool(os.getenv("MAIL_USE_TLS"))
    MAIL_USE_SSL = str_to_bool(os.getenv("MAIL_USE_SSL"))

    