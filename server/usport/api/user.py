#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
import json
import werkzeug
from flask import jsonify, request
from flask_restful import Resource, reqparse, abort, marshal_with, fields

# from ..models import Club as ClubModel
from ..models import User as UserModel

from ..utils.errors import ValidationError
from ..utils.decorators import login_required


class UserUpdate(Resource):
    # @login_required
    # def get(self):
    #     result = []
    #     for club in ClubModel.query.all():
    #         result.append(club.serialize())
    #     return {'data': result}

    @login_required
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('username', type=unicode)
        parser.add_argument('email', type=str)
        parser.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files')
        args = parser.parse_args()

        username = args.get('username')
        email = args.get('email')
        image = args.get('image')

        return
        try:
            UserModel.update(
                username=username,
                email=email,
            )
            return True, 200
        except ValidationError as e:
            abort(400, message='Алдаа -> {}'.format(str(e)))
