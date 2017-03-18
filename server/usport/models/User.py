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
    phone = Column(db.String(20), nullable=False)
    active = Column(db.Boolean(), default=True)
    isAdmin = Column(db.Boolean(), default=False)
    createdOn = Column(db.DateTime, nullable=False, server_default=db.func.now())
    updatedOn = Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

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

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'phone': self.phone,
            'active': self.active,
            'isAdmin': self.isAdmin,
            'createdOn': self.createdOn.strftime('%Y-%m-%d %H:%M'),
            'updatedOn': self.updatedOn.strftime('%Y-%m-%d %H:%M'),
        }
