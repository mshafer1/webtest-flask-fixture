import pytest
from webtest_flask_fixture import test_app

def test_can_load_test_index(mock_site, test_app):
    index = test_app.get('/')
    assert 'Hello, World!' in index  # string must be present in body

def test_can_load_test_js_file(mock_site, test_app):
    script = test_app.get('/scripts/script.js')
    assert 'console.log(' in script  # string must be present in body

def test_can_press_test_button(mock_site, test_app):
    page = test_app.get('/')
    page = page.click('Page 2')
    assert 'Page Two' in page
