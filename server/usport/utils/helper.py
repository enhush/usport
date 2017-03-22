#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from flask import current_app
from werkzeug import secure_filename

from .errors import ValidationError

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def is_allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def saveProfileImage(image):
    if image and is_allowed(image.filename):
        _dir = os.path.join(current_app.config['APP_DIR'], 'static', current_app.config['PROFILE_IMAGE_DIR'])

        if not os.path.isdir(_dir):
            os.mkdir(_dir)

        filename = secure_filename(image.filename)
        to_path = os.path.join(_dir, filename)
        image.save(to_path)
        # fileuri = os.path.join('/', current_app.config['PROFILE_IMAGE_DIR'], filename)

        return filename
    raise ValidationError('Файл тохиромжгүй')


def deleteProfileImage(image):
    if image:
        _dir = os.path.join(current_app.config['APP_DIR'], 'static', current_app.config['PROFILE_IMAGE_DIR'], image)
        if os.path.isfile(_dir):
            os.remove(_dir)
    return
