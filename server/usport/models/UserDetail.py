#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
from jose import jwt

from flask import current_app
from ..database import Column, Model, SurrogatePK, db, reference_col, relationship
from ..extensions import bcrypt
from ..utils.errors import ValidationError


class UserDetail(SurrogatePK, Model):

    __tablename__ = 'tb_users_detail'

    register = Column(db.String(20), unique=True, nullable=False)
    familyname = Column(db.String(80), nullable=False)
    lastname = Column(db.String(80), nullable=False)
    firstname = Column(db.String(80), nullable=False)
    sex = Column(db.Boolean(), default=False)  # 0 - male, 1 - female
    birthday = Column(db.Date, nullable=False)
    phone = Column(db.String(20), nullable=False)
    address = Column(db.String(200), nullable=False)
    email = Column(db.String(80), nullable=False)
    image = Column(db.String(250), nullable=True)
    sportTypeId = reference_col('tb_sport_types')
    clubId = reference_col('tb_clubs')
    userId = reference_col('tb_users')
    contactName = Column(db.String(80), nullable=False)
    contactPhone = Column(db.String(20), nullable=False)
    contactAddress = Column(db.String(200), nullable=False)

    active = Column(db.Boolean(), default=True)
    createdOn = Column(db.DateTime, nullable=False, server_default=db.func.now())
    updatedOn = Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    sportType = relationship("SportType", backref="userDetails")
    club = relationship("Club", backref="userDetails")
    user = relationship("User", backref="userDetails")

    def serialize(self):
        return {
            'id': self.id,
            'register': self.register,
            'familyname': self.familyname,
            'lastname': self.lastname,
            'firstname': self.firstname,
            'sex': self.sex,
            'birthday': self.birthday.strftime('%Y-%m-%d'),
            'phone': self.phone,
            'address': self.address,
            'email': self.email,
            'club': self.club.serialize(),
            'sportType': self.sportType.serialize(),
            'user': self.user.serialize(),
            'contactName': self.contactName,
            'contactPhone': self.contactPhone,
            'contactAddress': self.contactAddress,

            'createdOn': self.createdOn.strftime('%Y-%m-%d %H:%M'),
            'updatedOn': self.updatedOn.strftime('%Y-%m-%d %H:%M'),
        }
