"""Flask configuration."""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig(object):
    TESTING = os.environ.get("TESTING")
    DEBUG = os.environ.get("DEBUG")
    FLASK_ENV = os.environ.get("FLASK_ENV")
    FLASK_APP = os.environ.get("FLASK_APP")
    SECRET_KEY = os.environ.get("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(object):
    TESTING = "TESTING"
    DEBUG = "DEBUG"
    FLASK_ENV = "development"
    FLASK_APP = "app"
    SECRET_KEY = "SECRET_KEY"

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "test_database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
