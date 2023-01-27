import pytest

import sys

from src import create_app

@pytest.fixture
def test_client():

    # Create a Flask app configured for testing
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!

