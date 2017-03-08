#!/usr/bin/env python
# -*- coding: utf-8 -*-
from jose import jwt
from jose.exceptions import JWTError
from functools import wraps

from flask import current_app, request, g
from flask_restful import abort

from ..models.User import User


def login_required(f):
    @wraps(f)
    def func(*args, **kwargs):

        try:
            if 'Authorization' not in request.headers:
                abort(404, message="Нэвтрэх эрхгүй")
            token = request.headers.get('Authorization')[7:]
            payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            _id = payload['id']
            g.user = User.get_by_id(_id)
            if g.user is None:
                abort(404, message="Нэвтрэх эрхгүй")
            return f(*args, **kwargs)
        except JWTError as e:
            abort(400, message="Алдаа -> {}".format(str(e)))

    return func
