from flask import (
    request,
    jsonify,
    render_template
)
from api.extensions import db
import datetime


from flask_restful import Resource
from flask_jwt_extended import create_access_token, decode_token
from mods.users.models.user_model import UserModel, user_schema
from utils.errors import errors, error_handle
from flask_bcrypt import check_password_hash, generate_password_hash
from sqlalchemy.exc import IntegrityError
from jwt.exceptions import ExpiredSignatureError, DecodeError, \
    InvalidTokenError
from api.mail_service import send_email


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
                db.session.rollback()
                return jsonify(errors["SchemaValidationError"])
        except IntegrityError:
            db.session.rollback()
            return jsonify(errors["EmailAlreadyExistsError"])
        except Exception as e:
            db.session.rollback()
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


class ForgotPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'
        try:
            email = request.json['email']
            if not email:
                return jsonify(errors["SchemaValidationError"])

            user = UserModel.query.filter_by(email=request.json['email']).first()
            if not user:
                return jsonify(errors["EmailDoesnotExistsError"])

            expires = datetime.timedelta(hours=24)
            reset_token = create_access_token(str(user.id), expires_delta=expires)

            return send_email('Reset Your Password',
                              sender='winnyboy5@gmail.com',
                              recipients=[user.email],
                              text_body=render_template('email/reset_password.txt',
                                                        url=url + reset_token),
                              html_body=render_template('email/reset_password.html',
                                                        url=url + reset_token))

        except Exception as e:
            return error_handle(e)


class ResetPassword(Resource):
    def post(self):
        # url = request.host_url + 'reset/'
        try:
            reset_token = request.json['reset_token']
            password = request.json['password']

            if not reset_token or not password:
                return jsonify(errors["SchemaValidationError"])

            user_id = decode_token(reset_token)['identity']

            user = UserModel.query.filter_by(id=user_id).first()

            user.password = generate_password_hash(password).decode('utf8')
            db.session.commit()

            return send_email('[Movie-bag] Password reset successful',
                              sender='support@movie-bag.com',
                              recipients=[user.email],
                              text_body='Password reset was successful',
                              html_body='<p>Password reset was successful</p>')

        except ExpiredSignatureError:
            return jsonify(errors["ExpiredTokenError"])
        except (DecodeError, InvalidTokenError):
            return jsonify(errors["BadTokenError"])
        except Exception as e:
            return error_handle(e)
