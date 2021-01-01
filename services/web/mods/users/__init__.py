from flask import (
    request
)
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from api.extensions import db
from mods.users.models.user_model import UserModel, user_schema


users = {}


class UserResource(Resource):
    @jwt_required
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user_schema.dump([user])

    @jwt_required
    def patch(self, user_id):
        user = UserModel.query.get_or_404(user_id)

        if 'email' in request.json:
            user.email = request.json['email']
        if 'phone' in request.json:
            user.phone = request.json['phone']

        db.session.commit()
        return user_schema.dump([user])

    @jwt_required
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204
