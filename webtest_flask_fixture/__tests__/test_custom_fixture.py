import pytest

from webtest_flask_fixture import fixture_template

@pytest.fixture
def test_custom_app():
    from webtest import TestApp

    class CustomApp(fixture_template.DefaultFlaskApp):
        def handle_path(self, path):
            if path == '/':
                return 'NULL'
            return super(CustomApp, self).handle_path(path)

    customApp = CustomApp()

    flask_app = customApp.flask
    app = TestApp(flask_app)
    return app


@pytest.mark.parametrize('path, expected', [
    ('/', 'NULL'),
    ('/page_two/', 'Page Two'),
])
def test_can_press_test_button(mock_site, test_custom_app, path, expected):
    # Act
    resp = test_custom_app.get(path)

    # Assert
    assert expected in resp
