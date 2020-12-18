import json


from flask import (
    Flask, 
    request, 
    jsonify,
    Response
)
from flask_restful import Resource, Api
from api import db
from api.mods.users.models.user_model import UserModel, user_schema


users = {}

class UserListResource(Resource):
    def get(self):
        users = UserModel.query.all()
        return user_schema.dump(users)

    def post(self):
        new_user = UserModel(
            email=request.json['email'],
            phone=request.json['phone'],
            password=request.json['password']
        )
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump([new_user])


class UserResource(Resource):
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user_schema.dump([user])

    def patch(self, user_id):
        user = UserModel.query.get_or_404(user_id)

        if 'email' in request.json:
            user.title = request.json['email']
        if 'phone' in request.json:
            user.content = request.json['phone']

        db.session.commit()
        return user_schema.dump(user)

    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204
