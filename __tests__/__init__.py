import pytest
from webtest_flask_fixture import test_app

def test_can_load_test_index(test_app):
    test_app.get('/')
