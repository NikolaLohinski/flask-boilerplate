# -*- coding: utf-8 -*-
"""
Pytest fixtures for unit testing of API

@author: NikolaLohinski (https://github.com/NikolaLohinski)
@date: 02/02/09
"""
import os
import time
import pytest
from core import create_app


SQLITE_FILE_PATH = f"{os.getcwd()}/test.db"


# testing using sqlite, which may not be the same as testing with postgres but
# for unit tests, this will do
@pytest.fixture(scope="session")
def client():
    config_dict = {
        "SQLALCHEMY_DATABASE_URI": f"sqlite:///{SQLITE_FILE_PATH}",
        "DEBUG": True,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }
    os.environ['DEFAULT_INVENTIONS_FILE_PATH'] = './data/inventions.json'
    app = create_app(config_dict)
    app.app_context().push()

    # wait for sqlite file to be created
    time.sleep(2)
    from core.models import db

    db.create_all()
    # for test client api reference
    # http://flask.pocoo.org/docs/1.0/api/#test-client
    client = app.test_client()
    yield client

    # remove the file
    os.remove(SQLITE_FILE_PATH)
