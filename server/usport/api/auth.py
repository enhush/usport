#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import g
from flask_restful import Resource, reqparse, abort, marshal_with, fields

from ..models import User
from ..utils.errors import ValidationError
from ..utils.decorators import login_required

login_serializer = {
    'token': fields.String,
    'user': fields.Nested({
        'username': fields.String,
        'email': fields.String,
        'role': fields.Integer(attribute='isAdmin'),
    })
}

user_serializer = {
    'user': fields.Nested({
        'username': fields.String,
        'email': fields.String,
        'role': fields.Integer(attribute='isAdmin'),
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
        parser.add_argument('phone', type=str, help="Утасны дугаар оруулна уу!", required=True)
        parser.add_argument('isAdmin', type=int, choices=[0, 2], default=False)

        args = parser.parse_args()

        username = args.get('username')
        email = args.get('email')
        password = args.get('password')
        phone = args.get('phone')
        isAdmin = args.get('isAdmin')
        try:
            User.create(
                email=email,
                password=password,
                username=username,
                phone=phone,
                isAdmin=isAdmin,  # TODO just for testing
            )
            return True, 200
        except ValidationError as e:
            abort(400, message='Алдаа -> {}'.format(str(e)))
