from flask import (
    request, 
    Response,
    jsonify
)
from api import db
import datetime
import json


from flask_restful import Resource, Api
from flask_jwt_extended import create_access_token
from api.mods.users.models.user_model import UserModel, user_schema
from utils.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, \
InternalServerError
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
                raise SchemaValidationError

        except IntegrityError:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError

class LoginApi(Resource):
    def post(self):
        try:
            if((request.json['email'] or request.json['phone']) and request.json['password']):

                if request.json['email']:
                    user = UserModel.query.filter_by(email=request.json['email']).first()
                elif request.json['phone']:
                    user = UserModel.query.filter_by(phone=request.json['phone']).first()

                authorized = check_password_hash(user.password,request.json['password'])
                if not authorized:
                    raise UnauthorizedError

                expires = datetime.timedelta(days=7)
                access_token = create_access_token(identity=str(user.id), expires_delta=expires)
                return {'token': access_token}, 200
            else:
                raise UnauthorizedError

        except UnauthorizedError:
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError