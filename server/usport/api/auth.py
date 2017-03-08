#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import g
from flask_restful import Resource, reqparse, abort, marshal_with, fields

from ..models.User import User
from ..utils.errors import ValidationError
from ..utils.decorators import login_required

login_serializer = {
    'token': fields.String,
    'user': fields.Nested({
        'username': fields.String,
        'email': fields.String,
        'role': fields.Integer(attribute='is_admin'),
    })
}

user_serializer = {
    'user': fields.Nested({
        'username': fields.String,
        'email': fields.String,
        'role': fields.Integer(attribute='is_admin'),
    })
}


class AuthLogin(Resource):
    @marshal_with(login_serializer)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, help="И-мэйл оруулна уу", required=True)
        parser.add_argument('password', type=str, help="Нууц үг оруулна уу", required=True)

        args = parser.parse_args()

        email = args.get('email')
        password = args.get('password')

        try:
            token, user = User.validate(email, password)
            return {'token': token, 'user': user}
        except ValidationError as e:
            abort(400, message='Алдаа -> {}'.format(str(e)))


class AuthMe(Resource):

    @login_required
    @marshal_with(user_serializer)
    def get(self):
        return {'user': g.user}


class AuthRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help="Хэрэглэгчийн нэр оруулна уу!", required=True)
        parser.add_argument('email', type=str, help="И-мэйл оруулна уу!", required=True)
        parser.add_argument('password', type=str, help="Нууц үг оруулна уу!", required=True)

        args = parser.parse_args()

        username = args.get('username')
        email = args.get('email')
        password = args.get('password')

        try:
            User.create(
                email=email,
                password=password,
                username=username,
                is_admin=True,  # TODO just for testing
            )
            return {'message': 'Successfully created'}
        except ValidationError as e:
            abort(400, message='Алдаа -> {}'.format(str(e)))
