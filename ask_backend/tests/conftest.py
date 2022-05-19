import pytest

from ask_backend.app import create_app
from ask_backend.app import db as app_db
from ask_backend.users.models import User

DUMMY_USERNAME = "dummy_username"
DUMMY_EMAIL = "dummy@email.com"
DUMMY_FIRSTNAME = "dummy_firstname"
DUMMY_LASTNAME = "dummy_lastname"


@pytest.fixture
def app():
    app = create_app("config.TestingConfig")
    app_db.create_all(app=app)
    yield app
    app_db.drop_all(app=app)


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def session(app):
    return app_db.session


@pytest.fixture()
def user(session):
    user = User(
        username=DUMMY_USERNAME,
        email=DUMMY_EMAIL,
        firstname=DUMMY_FIRSTNAME,
        lastname=DUMMY_LASTNAME,
    )
    session.add(user)
    session.commit()
    return User.query.get(user.id)
