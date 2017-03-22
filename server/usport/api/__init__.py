#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, Blueprint
from flask_restful import Api

import auth
import club
import judge
import sportType
import judgeLevel
import user
import userDetail

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

api.add_resource(club.Club, '/club')
api.add_resource(judge.Judge, '/judge')
api.add_resource(sportType.SportType, '/sportType')
api.add_resource(judgeLevel.JudgeLevel, '/judgeLevel')
api.add_resource(user.User, '/user')
api.add_resource(user.Login, '/login')
api.add_resource(userDetail.UserDetail, '/user-detail')
api.add_resource(userDetail.UserDetailUpdate, '/user-detail-update')
