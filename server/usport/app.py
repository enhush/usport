#!/usr/bin/env python
# -*- coding: utf-8 -*-
import api
from flask import Flask, render_template

from .extensions import bcrypt, db, migrate
from .settings import ProdConfig


def create_app(config_object=ProdConfig):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    return None


def register_blueprints(app):
    app.register_blueprint(api.blueprint)
    return None
