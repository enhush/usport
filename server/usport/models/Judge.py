#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
from jose import jwt

from flask import current_app
from ..database import Column, Model, SurrogatePK, db, reference_col, relationship
from ..extensions import bcrypt
from ..utils.errors import ValidationError


class Judge(SurrogatePK, Model):

    __tablename__ = 'tb_judges'

    lastname = Column(db.String(80), nullable=False)
    firstname = Column(db.String(80), nullable=False)
    phone = Column(db.String(20), nullable=False)
    judgeLevelId = reference_col('tb_judge_levels')
    sportTypeId = reference_col('tb_sport_types')
    clubId = reference_col('tb_clubs')
    createdOn = Column(db.DateTime, nullable=False, server_default=db.func.now())
    updatedOn = Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    judgeLevel = relationship("JudgeLevel", backref="judges")
    sportType = relationship("SportType", backref="judges")
    club = relationship("Club", backref="judges")

    def serialize(self):
        return {
            'id': self.id,
            'lastname': self.lastname,
            'firstname': self.firstname,
            'phone': self.phone,
            'judgeLevel': self.judgeLevel.serialize(),
            'sportType': self.sportType.serialize(),
            'club': self.club.serialize(),
            'createdOn': self.createdOn.strftime('%Y-%m-%d %H:%M'),
            'updatedOn': self.updatedOn.strftime('%Y-%m-%d %H:%M'),
        }
