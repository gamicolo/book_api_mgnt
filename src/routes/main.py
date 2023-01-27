from flask import Blueprint, request, jsonify
from src.extensions import db
from src.models import Book
import requests
import os
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')
logger = logging.getLogger('models_main')

main = Blueprint('main', __name__)

BOOK_API_URL=os.getenv('BOOK_API_URL') or "https://openlibrary.org/isbn/"

@main.route('/api/v1/assessment/get_book_info/<string:book_isbn>', methods=['GET','OPTIONS'])
def get_book_info(book_isbn):

    if request.method == 'GET':

        code = 404
        reply = f"Could not retrieve the info of the book with ISBN <{book_isbn}>"
        
        book_stored = Book.query.filter(Book.isbn == book_isbn).first()

        if book_stored:
            code = 200
            reply = book_stored.info 
            logging.debug(f"Retrieve info of the book with ISBN <{book_isbn}> from the database")
        else:
            url = f"{BOOK_API_URL}/{book_isbn}.json"
            try:
                book_info = requests.get(url)
                code = book_info.status_code
                reply = book_info.json()
            except:
                logging.error(f"Could not get the info for the book with ISBN <{book_isbn}> from the URL <{url}>")
            
        return jsonify(reply),code

    return "",200

@main.route('/api/v1/assessment/store_book_info/<string:book_isbn>', methods=['POST','OPTIONS'])
def store_book_info(book_isbn):

    code = 200
    reply = f"Book with ISBN <{book_isbn}> stored succesfully on the database"

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
                logging.error(f"Couldn't store the book with ISBN <{book_isbn}> on the database")
                code = 503
                reply = f"Could not store book book with ISBN <{book_isbn}> on the database"


        else:
            logging.debug(f"The book with ISBN <{book_isbn}> already exist on the database")
            reply = f"Book with ISBN <{book_isbn}> already exist on the database"

        return jsonify(reply),code

    return "",200

@main.route('/api/v1/assessment/get_books', methods=['GET','OPTIONS'])
def get_books():

    if request.method == 'GET':

        code = 200
        
        book_list=None
        if request.headers.get('Content-Type'):
            book_list = request.json.get('books')

        if book_list:
            books = Book.query.filter(Book.isbn.in_(book_list)).all()
        else:
            books = Book.query.all()

        return jsonify([book.info for book in books]),code


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
            reply = 'Success updating the comment in the book'
        except:
            reply = 'ERROR trying to update the comment of the book on the database'
            logging.error(f"Couldn't update the comments of the book with ISBN <{book_isbn}> on the database")

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
            logging.error(f"Couldn't delete the comments of the book with ISBN <{book_isbn}> on the database")

        return jsonify(reply),code

    return "",200
