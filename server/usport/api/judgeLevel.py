#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
import json
from flask import jsonify
from flask_restful import Resource, reqparse, abort, marshal_with, fields

from ..models import JudgeLevel as JudgeLevelModel

from ..utils.errors import ValidationError
from ..utils.decorators import login_required


class JudgeLevel(Resource):
    @login_required
    def get(self):
        result = []
        for judgeLevel in JudgeLevelModel.query.all():
            result.append(judgeLevel.serialize())
        return {'data': result}
