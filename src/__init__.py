from flask import Flask

from .commands import create_tables
from .extensions import db
from .models import Book
from .routes.main import main

def create_app(config_file='settings.py'):

    """ Creates and returns a Flask application using the application factory pattern """

    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(main)
    app.cli.add_command(create_tables)

    return app
