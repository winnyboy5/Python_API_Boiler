import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/api/static/"
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/api/media/"
    SECRET_KEY = '34a19f17d155f928c31bd1f6de8de16f2ca1d3d7605f3278'