from flask import (
    request,
    jsonify
)
from api import db
import datetime


from flask_restful import Resource
from flask_jwt_extended import create_access_token
from mods.users.models.user_model import UserModel, user_schema
from utils.errors import errors, error_handle
from flask_bcrypt import check_password_hash
from sqlalchemy.exc import IntegrityError


class SignupApi(Resource):
    def post(self):
        try:
            if(request.json['email'] and request.json['phone'] and request.json['password']):
                new_user = UserModel(
                    email=request.json['email'],
                    phone=request.json['phone'],
                    password=request.json['password']
                )
                db.session.add(new_user)
                db.session.commit()
                return user_schema.dump([new_user]), 200
            else:
                return jsonify(errors["SchemaValidationError"])
        except IntegrityError:
            return jsonify(errors["EmailAlreadyExistsError"])
        except Exception as e:
            return error_handle(e)


class LoginApi(Resource):
    def post(self):
        try:
            if((request.json['email'] or request.json['phone']) and request.json['password']):

                if request.json['email']:
                    user = UserModel.query.filter_by(email=request.json['email']).first()
                elif request.json['phone']:
                    user = UserModel.query.filter_by(phone=request.json['phone']).first()

                authorized = check_password_hash(user.password, request.json['password'])
                if not authorized:
                    return jsonify(errors["UnauthorizedError"])

                expires = datetime.timedelta(days=7)
                access_token = create_access_token(identity=str(user.id), expires_delta=expires)
                return {'token': access_token}, 200
            else:
                return jsonify(errors["UnauthorizedError"])

        except Exception as e:
            return error_handle(e)
