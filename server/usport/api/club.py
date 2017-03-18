#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
import json
from flask import jsonify
from flask_restful import Resource, reqparse, abort, marshal_with, fields

from ..models import Club as ClubModel
from ..models import User

from ..utils.errors import ValidationError
from ..utils.decorators import login_required


class Club(Resource):
    @login_required
    def get(self):
        result = []
        for club in ClubModel.query.all():
            result.append(club.serialize())
        return {'data': result}

    @login_required
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('founder', type=unicode, help="Үүсгэн байгуулагч оруулна уу", required=True, location='json')
        parser.add_argument('createdDate', type=str, help="Үүсгэсэн огноо", required=True)
        parser.add_argument('name', type=unicode, help="Нэр оруулна уу", required=True)
        parser.add_argument('email', type=str, help="И-мэйл оруулна уу", required=True)
        parser.add_argument('website', type=str, help="Вэбсайт оруулна уу", required=True)
        parser.add_argument('address', type=unicode, help="Хаяг оруулна уу", required=True)
        parser.add_argument('phone', type=str, help="Утас оруулна уу", required=True)
        parser.add_argument('organiserName', type=unicode, help="Зохион байгуулагчийн нэр оруулна уу", required=True)
        parser.add_argument('organiserEmail', type=str, help="Зохион байгуулагчийн и-мэйл оруулна уу", required=True)
        parser.add_argument('organiserPhone', type=str, help="Зохион байгуулагчийн утас оруулна уу", required=True)

        args = parser.parse_args()

        founder = args.get('founder')
        createdDate = args.get('createdDate')
        name = args.get('name')
        email = args.get('email')
        website = args.get('website')
        address = args.get('address')
        phone = args.get('phone')
        organiserName = args.get('organiserName')
        organiserEmail = args.get('organiserEmail')
        organiserPhone = args.get('organiserPhone')

        createdDate = dt.datetime.strptime(createdDate, "%Y-%m-%d").date()
        try:
            ClubModel.create(
                founder=founder,
                createdDate=createdDate,
                name=name,
                email=email,
                website=website,
                address=address,
                phone=phone,
                organiserName=organiserName,
                organiserEmail=organiserEmail,
                organiserPhone=organiserPhone,
            )
            return True, 200
        except ValidationError as e:
            abort(400, message='Алдаа -> {}'.format(str(e)))
