from api.extensions import db, ma
from utils.db_utils import TimestampMixin


class UserModel(db.Model, TimestampMixin):
    __tablename__ = "users"

    email = db.Column(db.String(128), unique=True, nullable=False)
    phone = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, **kwargs):
        super(UserModel, self).__init__(**kwargs)


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "email", "phone", "active", "created_at", "updated_at")


user_schema = UserSchema()
user_schema = UserSchema(many=True)
