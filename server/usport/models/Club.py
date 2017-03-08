#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
from jose import jwt

from flask import current_app
from ..database import Column, Model, SurrogatePK, db, reference_col, relationship
from ..utils.errors import ValidationError


class Club_(SurrogatePK, Model):

    __tablename__ = 'tb_clubs'

    founder = Column(db.String(80), nullable=False)
    createdDate = Column(db.Date, nullable=False)
    name = Column(db.String(80), nullable=False)
    email = Column(db.String(80), nullable=False)
    website = Column(db.String(80), nullable=False)
    address = Column(db.String(200), nullable=False)
    phone = Column(db.String(20), nullable=False)
    organiserName = Column(db.String(80), nullable=False)
    organiserEmail = Column(db.String(80), nullable=False)
    organiserPhone = Column(db.String(20), nullable=False)
