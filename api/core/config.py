# -*- coding: utf-8 -*-
"""
Flask configuration definitions

@author: NikolaLohinski (https://github.com/NikolaLohinski)
@date: 02/02/09
"""
import os

USER = os.environ.get('POSTGRES_USER')
PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DATABASE = os.environ.get('POSTGRES_DB')


class Config:
    """Basic master config class to inherit from"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE = 'api.log'


class DevelopmentConfig(Config):
    """Development configuration to start with"""
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@postgres/{}'.format(
        USER, PASSWORD, DATABASE
    )
    DEBUG = True


config = {
    'dev': DevelopmentConfig
}
