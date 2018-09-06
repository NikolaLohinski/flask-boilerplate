import os

USER = os.environ.get('POSTGRES_USER')
PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DATABASE = os.environ.get('POSTGRES_DB')


class Config:
    SECRET_KEY = 'testkey'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE = 'api.log'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@postgres/{}'.format(
        USER, PASSWORD, DATABASE
    )
    DEBUG = True


config = {
    'dev': DevelopmentConfig
}
