#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_bcrypt import Bcrypt
# from flask_caching import Cache
# from flask_debugtoolbar import DebugToolbarExtension
# from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from flask_wtf.csrf import CSRFProtect

bcrypt = Bcrypt()
# csrf_protect = CSRFProtect()
# login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
# cache = Cache()
# debug_toolbar = DebugToolbarExtension()
