import os 

BASEDIR = os.path.abspath(os.path.dirname(__file__))

DB_NAME = os.environ.get('SQLALCHEMY_DATABASE_NAME') or 'db.sqlite3'
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASEDIR, DB_NAME)}"
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False

