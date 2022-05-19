import pytest
from ask_backend.users.models import User
from ask_backend.app import create_app, db


@pytest.fixture
def app():
    app = create_app("config.TestingConfig")
    db.create_all(app=app)
    yield app
    db.drop_all(app=app)


@pytest.fixture()
def client(app):
    return app.test_client()

