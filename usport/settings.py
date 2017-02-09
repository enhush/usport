# -*- coding: utf-8 -*-

"""Configurations"""
import os


class Config(object):
    """Basic"""

    SECRET_KEY = os.environ.get('USPORT_SECRET', 'A0ZrmN]LWX/,?RT98j/3yX R~XHH!j')  # TODO: Change
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))


class ProdConfig(Config):
    """Production"""

    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ''    # TODO: Change
    ASSETS_DEBUG = False


class DevConfig(Config):
    """Development"""

    ENV = 'dev'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format('')    # TODO: Change
    ASSETS_DEBUG = True  # Don't bundle/minify static assets
