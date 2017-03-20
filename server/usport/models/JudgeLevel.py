#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
from jose import jwt

from flask import current_app
from ..database import Column, Model, SurrogatePK, db, reference_col, relationship
from ..extensions import bcrypt
from ..utils.errors import ValidationError


class JudgeLevel(SurrogatePK, Model):

    __tablename__ = 'tb_judge_levels'

    name = Column(db.String(80), nullable=False)
    active = Column(db.Boolean(), default=True)
    createdOn = Column(db.DateTime, nullable=False, server_default=db.func.now())
    updatedOn = Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'createdOn': self.createdOn.strftime('%Y-%m-%d %H:%M'),
            'updatedOn': self.updatedOn.strftime('%Y-%m-%d %H:%M'),
        }
