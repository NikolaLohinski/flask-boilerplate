# -*- coding: utf-8 -*-
"""
Flask Script Manager to start server and run commands
@author: NikolaLohinski (https://github.com/NikolaLohinski)
@date: 02/02/09
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from core import create_app
from core.views import v0
from core.models import db

app = create_app()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)


@manager.command
def runserver():
    app.run(debug=True, host="0.0.0.0", port=5000)


@manager.command
def recreate_db():
    """
    Recreates a local database. You probably should not use this on
    production.
    """
    v0.re_init_db()


if __name__ == "__main__":
    manager.run()
