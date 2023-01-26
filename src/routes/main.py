from flask import Blueprint, request, jsonify
from src.extensions import db
from src.models import Book
import requests

main = Blueprint('main', __name__)

BOOK_API="https://openlibrary.org/isbn/"

@main.route('/api/v1/assessment/get_book_info/<string:book_isbn>', methods=['GET','OPTIONS'])
def get_book_info(book_isbn):

    if request.method == 'GET':

        code = 404
        reply = {"The book doesn't exist on the database"}
        
        book_stored = Book.query.filter(Book.isbn == book_isbn).first()

        if book_stored:
            code = 200
            reply = book_stored.info 
        else:
            url = f"{BOOK_API}/{book_isbn}.json"
            try:
                book_info = requests.get(url)
                code = 200
                reply = book_info.json()
            except:
                print("ERROR")
            
        return jsonify(reply),code

    return "",200

@main.route('/api/v1/assessment/store_book_info/<string:book_isbn>', methods=['POST','OPTIONS'])
def store_book_info(book_isbn):

    if request.method == 'POST':

        book_info = str(request.json['book_info'])
        book_comments = request.json['book_comments'] 

        book = Book(
            isbn = book_isbn,
            info = book_info,
            comments = book_comments
        )

        if not(Book.query.filter(Book.isbn == book_isbn).first()):
            try:
                db.session.add(book)
                db.session.commit()
            except:
                print('ERROR trying to store the book info on the DB' )

        else:
            print('ERROR: ISBN already exists on the DB')

        return jsonify("Done"),200

    return "",200

@main.route('/api/v1/assessment/book_comments_management/<string:book_isbn>', methods=['GET','PUT','DELETE','OPTIONS'])
def book_comments_management(book_isbn):

    code = 404
    reply = "The book doesn't exist on the database"
    
    book_stored = Book.query.filter(Book.isbn == book_isbn).first()

    if not(book_stored):
        return jsonify(reply),code

    if request.method == 'PUT':
        book_stored.comments = request.json['book_comments']
        try:
            db.session.commit()
            code = 200
            reply = 'Success update of the comment in the book'
        except:
            reply = 'ERROR trying to update the comment of the book on the DB'
            print(reply)

        return jsonify(reply),code

    if request.method == 'GET':
        code = 200
        reply = 'Success getting the comment of the book'

        return jsonify(book_stored.comments),code

    if request.method == 'DELETE':
        book_stored.comments = '' 
        try:
            db.session.commit()
            code = 200
            reply = 'Success deleting the comment of the book'
        except:
            reply = 'ERROR trying to delete the comment of the book'
            print(reply)

        return jsonify(reply),code

    return "",200
