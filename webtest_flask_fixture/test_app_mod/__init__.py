from webtest_flask_fixture import fixture_template
import pytest

@pytest.fixture
def test_app():
    from webtest import TestApp

    class Wrapper(fixture_template.FlaskWrapper):
        pass

    wrapper = Wrapper()

    flask_app = wrapper.app
    app = TestApp(flask_app)
    return app
