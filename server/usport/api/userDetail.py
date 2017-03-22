#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
import json
import werkzeug
from flask import jsonify, request, g
from flask_restful import Resource, reqparse, abort, marshal_with, fields

# from ..models import Club as ClubModel
from ..models import UserDetail as UserDetailModel

from ..utils.errors import ValidationError
from ..utils.decorators import login_required
from ..utils.helper import saveProfileImage, deleteProfileImage


class UserDetail(Resource):
    @login_required
    def get(self):
        userDetail = UserDetailModel.query.filter_by(user=g.user).first()
        if userDetail:
            return {'userDetail': userDetail.serialize()}
        abort(400, message='Алдаа -> {}'.format(str('Мэдээлэл байхгүй')))


class UserDetailUpdate(Resource):
    @login_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('register', type=unicode, help="Регистрийн дугаар оруулна уу!", required=True)
        parser.add_argument('familyname', type=unicode, help="Ургийн овог оруулна уу!", required=True)
        parser.add_argument('lastname', type=unicode, help="Овог оруулна уу!", required=True)
        parser.add_argument('firstname', type=unicode, help="Нэр оруулна уу!", required=True)
        parser.add_argument('sex', type=bool, help="Хүйс оруулна уу!", required=True)
        parser.add_argument('birthday', type=str, help="Төрсөн өдөр оруулна уу!", required=True)
        parser.add_argument('phone', type=str, help="Утас оруулна уу!", required=True)
        parser.add_argument('address', type=unicode, help="Хаяг оруулна уу!", required=True)
        parser.add_argument('email', type=str, help="Хаяг оруулна уу!", required=True)
        parser.add_argument('sportTypeId', type=int, help="Спортын төрөл оруулна уу!", required=True)
        parser.add_argument('clubId', type=int, help="Харьяа клуб оруулна уу!", required=True)
        parser.add_argument('contactName', type=unicode, help="Холбоо барих хүний нэр оруулна уу!", required=True)
        parser.add_argument('contactPhone', type=str, help="Холбоо барих хүний утас оруулна уу!", required=True)
        parser.add_argument('contactAddress', type=unicode, help="Холбоо барих хүний хаяг оруулна уу!", required=True)
        parser.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files')

        args = parser.parse_args()

        register = args.get('register')
        familyname = args.get('familyname')
        lastname = args.get('lastname')
        firstname = args.get('firstname')
        sex = args.get('sex')
        birthday = args.get('birthday')
        phone = args.get('phone')
        address = args.get('address')
        email = args.get('email')
        sportTypeId = args.get('sportTypeId')
        clubId = args.get('clubId')
        contactName = args.get('contactName')
        contactPhone = args.get('contactPhone')
        contactAddress = args.get('contactAddress')
        image = args.get('image')

        birthday = dt.datetime.strptime(birthday, "%Y-%m-%d").date()

        try:
            userDetail = UserDetailModel.query.get(g.user.id)

            image = saveProfileImage(image) if image else userDetail.image
            deleteProfileImage(userDetail.image)
            userDetail.update(
                register=register,
                familyname=familyname,
                lastname=lastname,
                firstname=firstname,
                sex=sex,
                birthday=birthday,
                phone=phone,
                address=address,
                email=email,
                image=image,
                sportTypeId=sportTypeId,
                clubId=clubId,
                contactName=contactName,
                contactPhone=contactPhone,
                contactAddress=contactAddress,
            )
            return {'userDetail': userDetail.serialize()}
        except ValidationError as e:
            abort(400, message='Алдаа -> {}'.format(str(e)))
