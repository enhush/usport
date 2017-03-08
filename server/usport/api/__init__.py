#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, Blueprint
from flask_restful import Api

import auth
import club

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

api.add_resource(auth.AuthLogin, '/auth/login')
api.add_resource(auth.AuthRegister, '/auth/register')
api.add_resource(auth.AuthMe, '/auth/me')

api.add_resource(club.Club, '/club')
