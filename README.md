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

(venv) $ flask run

Navigate to 'http://127.0.0.1:5000' in your favorite web browser to view the website!

# Testing
To run all the tests:

(venv) $ python -m pytest -v

To check the code coverage of the tests:

(venv) $ python -m pytest --cov-report term-missing --cov=project
