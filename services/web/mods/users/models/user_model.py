from api import db, ma
from utils.db_utils import db_timestamp
from flask_bcrypt import generate_password_hash, check_password_hash


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    phone = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    db_timestamp(db)

    def __init__(self, email, phone, password):
        self.email = email
        self.phone = phone
        self.password = generate_password_hash(password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "email", "phone", "active", "created_at", "updated_at")


user_schema = UserSchema()
user_schema = UserSchema(many=True)
