import pytest
from ask_backend.users.models import User


@pytest.fixture
def app():
    from ask_backend.app import create_app
    app = create_app("config.TestingConfig")
    return app


@pytest.fixture()
def client(app):
    return app.test_client()
