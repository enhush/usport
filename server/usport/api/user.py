#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
import json
import werkzeug
from flask import jsonify, request, g
from flask_restful import Resource, reqparse, abort, marshal_with, fields

# from ..models import Club as ClubModel
from ..models import User as UserModel

from ..utils.errors import ValidationError
from ..utils.decorators import login_required


class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, help="И-мэйл оруулна уу", required=True)
        parser.add_argument('password', type=str, help="Нууц үг оруулна уу", required=True)

        args = parser.parse_args()

        email = args.get('email')
        password = args.get('password')

        try:
            token, user = UserModel.validate(email, password)
            return {'token': token, 'user': user.serialize()}
        except ValidationError as e:
            abort(400, message='Алдаа -> {}'.format(str(e)))


class User(Resource):
    @login_required
    def get(self):
        return {'user': g.user.serialize()}

    @login_required
    def put(self):
        parser = reqparse.RequestParser()

        parser.add_argument('username', type=unicode)
        parser.add_argument('email', type=str)
        args = parser.parse_args()

        username = args.get('username')
        email = args.get('email')

        try:

            user = UserModel.query.get(g.user.id)
            user.update(
                username=username,
                email=email,
            )
            return {'user': user.serialize()}
        except ValidationError as e:
            abort(400, message='Алдаа -> {}'.format(str(e)))


# class AuthRegister(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('username', type=str, help="Хэрэглэгчийн нэр оруулна уу!", required=True)
#         parser.add_argument('email', type=str, help="И-мэйл оруулна уу!", required=True)
#         parser.add_argument('password', type=str, help="Нууц үг оруулна уу!", required=True)
#         parser.add_argument('phone', type=str, help="Утасны дугаар оруулна уу!", required=True)
#         parser.add_argument('isAdmin', type=int, choices=[0, 2], default=False)
#
#         args = parser.parse_args()
#
#         username = args.get('username')
#         email = args.get('email')
#         password = args.get('password')
#         phone = args.get('phone')
#         isAdmin = args.get('isAdmin')
#         try:
#             User.create(
#                 email=email,
#                 password=password,
#                 username=username,
#                 phone=phone,
#                 isAdmin=isAdmin,  # TODO just for testing
#             )
#             return True, 200
#         except ValidationError as e:
#             abort(400, message='Алдаа -> {}'.format(str(e)))
