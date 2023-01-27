# REST API for book management
Simple Rest API for book management

# Overview
This Flask application contains basic book management functionality (get and store books) and also allows CRUD operations over the book comments.

# Installation Instructions

## Installation
Pull down the source code from this GitLab repository:

$ git clone https://github.com/gamicolo/book_api_mgnt

Create a new virtual environment:

$ cd book_api_mgnt 
$ python3 -m venv venv

Activate the virtual environment:

$ source venv/bin/activate

Install the python packages specified in requirements.txt:

(venv) $ pip install -r requirements.txt

## Database Initialization

This Flask application needs a SQLite database to store data. The database should be initialized using:

(venv) $ flask create_tables

## Running the Flask Application

Run development server to serve the Flask application:

(venv) $ cd src/
(venv) $ flask run

To get book information use the folloiing instruction:
curl http://127.0.0.1:5000/api/v1/assessment/get_book_info/<book_isbn>'

Or navigate to 'http://127.0.0.1:5000/api/v1/assessment/get_book_info/<book_isbn>'

To store book information use the following instruction:

curl http://127.0.0.1:5000/api/v1/assessment/store_book_info/<book_isbn> -X PUT -H "Content-Type: application/json" -d '{"book_info":{"book title":"book1"},"comments":"first comment"}'

To get book information of a specific list of book, use:

curl http://127.0.0.1:5000/api/v1/assessment/get_books -X GET -H "Content-Type: application/json" -d '{"books":[<book_isbn1>,<book_isbn2>,...]}'

To get book information of the complete list of books in the database, use:

curl http://127.0.0.1:5000/api/v1/assessment/get_books -X GET

To update a comment use the following instruction:

curl http://127.0.0.1:5000/api/v1/assessment/book_comments_management/<book_isbn> -X PUT -H "Content-Type: application/json" -d '{"book_comments": "coment"}'      

To get a comment, use:

curl http://127.0.0.1:5000/api/v1/assessment/book_comments_management/<book_isbn> -X GET      

To delete a comment, use:

curl http://127.0.0.1:5000/api/v1/assessment/book_comments_management/<book_isbn> -X DELETE      

# Testing
To run all the tests:

(venv) $ python -m pytest -v

To check the code coverage of the tests:

(venv) $ python -m pytest --cov-report term-missing --cov=project
