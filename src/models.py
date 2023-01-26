from .extensions import db 

class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(50), unique=True)
    info = db.Column(db.String(2500))
    comments = db.Column(db.String(500))

