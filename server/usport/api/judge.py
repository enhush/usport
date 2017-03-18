#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
import json
from flask import jsonify
from flask_restful import Resource, reqparse, abort, marshal_with, fields

from ..models import Judge as JudgeModel

from ..utils.errors import ValidationError
from ..utils.decorators import login_required


class Judge(Resource):
    @login_required
    def get(self):
        result = []
        for judge in JudgeModel.query.all():
            result.append(judge.serialize())
        return {'data': result}

    @login_required
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('lastname', type=unicode, help="Овог оруулна уу", required=True)
        parser.add_argument('firstname', type=unicode, help="Нэр оруулна уу", required=True)
        parser.add_argument('phone', type=str, help="Утас оруулна уу", required=True)
        parser.add_argument('judgeLevelId', type=int, help="Зэрэг цол оруулна уу", required=True)
        parser.add_argument('sportTypeId', type=int, help="Спортын төрөл оруулна уу", required=True)
        parser.add_argument('clubId', type=int, help="Харьяа клуб оруулна уу", required=True)

        args = parser.parse_args()

        lastname = args.get('lastname')
        firstname = args.get('firstname')
        phone = args.get('phone')
        judgeLevelId = args.get('judgeLevelId')
        sportTypeId = args.get('sportTypeId')
        clubId = args.get('clubId')

        try:
            JudgeModel.create(
                lastname=lastname,
                firstname=firstname,
                phone=phone,
                judgeLevelId=judgeLevelId,
                sportTypeId=sportTypeId,
                clubId=clubId,
            )
            return True, 200
        except ValidationError as e:
            abort(400, message='Алдаа -> {}'.format(str(e)))
