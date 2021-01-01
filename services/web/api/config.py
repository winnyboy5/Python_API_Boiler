import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/api/static/"
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/api/media/"
    SECRET_KEY = '34a19f17d155f928c31bd1f6de8de16f2ca1d3d7605f3278'
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '582c1169b62dba'
    MAIL_PASSWORD = '954c6d89f7685c'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
