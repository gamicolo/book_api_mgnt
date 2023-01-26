from flask import Flask

from .commands import create_tables
from .extensions import db
#from .models import Users, UserSessions, Questions, Options, UserAnswers
from .models import Book
#from .routes.auth import auth
from .routes.main import main

def create_app(config_file='settings.py'):

    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    #login_manager = LoginManager()
    #login_manager.login_view = 'auth.register'
    #login_manager.init_app(app)

    #@login_manager.user_loader
    #def load_user(user_id):
    #    return Users.query.get(int(user_id))

    #app.register_blueprint(auth)
    app.register_blueprint(main)

    app.cli.add_command(create_tables)

    return app
