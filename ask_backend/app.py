from flask import Flask
from flask_migrate import Migrate


def create_app(config="config.DevelopmentConfig"):
    """
    create_app method create new flask app.
    :param config: environment configurations
    :return: app
    """

    app = Flask(__name__)
    if config == "config.DevelopmentConfig":
        app.config.from_object(config)
    else:
        app.config.from_mapping(
            DEBUG=True,
            TESTING=True,
            SECRET_KEY='dev',
            SQLALCHEMY_DATABASE_URI="postgresql://flask_user:flask_password@localhost:5432/test_db",
            SQLALCHEMY_TRACK_MODIFICATIONS=True,
        )

    """
    Database initialization and Migration
    """
    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy(app)
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app=app, db=db)
    """
    Register Blueprints
    """
    from ask_backend.core.routes import core_bp
    from ask_backend.errors.handlers import errors_bp
    from ask_backend.users.routes import user_bp

    app.register_blueprint(errors_bp)
    app.register_blueprint(core_bp)
    app.register_blueprint(user_bp)

    return app
