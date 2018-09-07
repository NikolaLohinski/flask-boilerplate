# -*- coding: utf-8 -*-
"""
Initialisation of Flask API

@author: NikolaLohinski (https://github.com/NikolaLohinski)
@date: 02/02/09
"""
import os
import logging

from flask import Flask, request
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy_utils import create_database, database_exists

from core.config import config
from core.utils import all_exception_handler


class RequestFormatter(logging.Formatter):
    """API request formater"""
    def format(self, record):
        record.url = request.url
        record.remote_addr = request.remote_addr
        return super().format(record)


def create_app(test_config=None):
    """Main initialisation function to call to start API
    :param test_config: optional test configuration
    :return: Flask.app: the Flask app
    """
    app = Flask(__name__)

    CORS(app)  # add CORS

    # check environment variables to see which config to load
    env = os.environ.get('FLASK_ENV', 'dev')
    if test_config:
        # ignore environment variable config if config was given
        app.config.from_mapping(**test_config)
    else:
        app.config.from_object(config[env])

    # decide whether to create database
    db_url = app.config['SQLALCHEMY_DATABASE_URI']
    if not database_exists(db_url):
        create_database(db_url)

    # register sqlalchemy to this app
    from core.models import db

    db.init_app(app)
    Migrate(app, db)

    # import and register blueprints
    from core.views import v0

    app.register_blueprint(v0.v0, url_prefix='/api/v0')

    # register error Handler
    app.register_error_handler(Exception, all_exception_handler)

    return app
