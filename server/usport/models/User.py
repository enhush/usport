#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
from jose import jwt

from flask import current_app
from ..database import Column, Model, SurrogatePK, db, reference_col, relationship
from ..extensions import bcrypt
from ..utils.errors import ValidationError


class User(SurrogatePK, Model):

    __tablename__ = 'tb_users'

    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(80), unique=True, nullable=False)
    password = Column(db.Binary(128), nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    active = Column(db.Boolean(), default=True)
    is_admin = Column(db.Boolean(), default=False)

    def __init__(self, username, email, password, **kwargs):
        db.Model.__init__(self, username=username, email=email, **kwargs)
        self.set_password(password)

    @classmethod
    def validate(cls, email, password):
        user = cls.query.filter_by(email=email).first()

        if not user:
            raise ValidationError("И-мэйл хаяг буруу")

        _id = user.id

        if user.check_password(password):
            try:
                token = jwt.encode({'id': _id}, current_app.config['SECRET_KEY'], algorithm='HS256')
                return token, user
            except JWTError:
                raise ValidationError('Алдаа')
        else:
            raise ValidationError('Нууц үг буруу')

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        return bcrypt.check_password_hash(self.password, value)
