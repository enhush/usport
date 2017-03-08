#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from usport.app import create_app
from usport.settings import DevConfig, ProdConfig
from usport.database import db

CONFIG = DevConfig  # ProdConfig

app = create_app(CONFIG)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/<path:path>')
def other(path):
    return render_template('index.html')

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def db_create():
    db.create_all()


@manager.command
def db_drop():
    db.drop_all()

if __name__ == '__main__':
    # app.run(debug=CONFIG.DEBUG, host='0.0.0.0')
    manager.run()
