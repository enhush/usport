#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
import json
from flask import jsonify
from flask_restful import Resource, reqparse, abort, marshal_with, fields

from ..models import SportType as SportTypeModel

from ..utils.errors import ValidationError
from ..utils.decorators import login_required


class SportType(Resource):
    @login_required
    def get(self):
        result = []
        for sportType in SportTypeModel.query.all():
            result.append(sportType.serialize())
        return {'data': result}
