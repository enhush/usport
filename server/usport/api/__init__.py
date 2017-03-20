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


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

api.add_resource(auth.AuthLogin, '/auth/login')
api.add_resource(auth.AuthRegister, '/auth/register')
api.add_resource(auth.AuthMe, '/auth/me')
api.add_resource(club.Club, '/club')
api.add_resource(judge.Judge, '/judge')
api.add_resource(sportType.SportType, '/sportType')
api.add_resource(judgeLevel.JudgeLevel, '/judgeLevel')
api.add_resource(user.UserUpdate, '/user-update')
