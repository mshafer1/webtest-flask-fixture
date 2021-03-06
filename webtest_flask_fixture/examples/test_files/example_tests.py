import pytest
from webtest_flask_fixture import test_app


def test_can_load_test_index(test_app):
    # Act
    resp = test_app.get('/')

    # Assert
    assert resp.status_int == 200
    assert resp.content_type == 'text/html'
    assert 'Hello, World!' in resp  # string must be present in body


def test_can_load_test_js_file(test_app):
    # Act
    resp = test_app.get('/scripts/script.js')

    # Assert
    assert resp.status_int == 200
    assert resp.content_type == 'application/javascript'
    assert 'console.log(' in resp  # string must be present in body


def test_can_press_test_button(test_app):
    # Arrange
    resp = test_app.get('/')

    # Act
    resp = resp.click('Page 2')

    # Assert
    assert resp.status_int == 200
    assert resp.content_type == 'text/html'
    assert 'Page Two' in resp


if __name__ == '__main__':
    pytest.main([__file__, '-s'])
