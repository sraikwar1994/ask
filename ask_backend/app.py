from flask import Flask

from .database import db, migrate


def create_app(config="config.DevelopmentConfig"):
    """
    create_app method create new flask app.
    :param config: environment configurations
    :return: app
    """

    app = Flask(__name__)
    if config == "ask_backend.config.DevelopmentConfig":
        app.config.from_object(config)
    else:
        app.config.from_pyfile("unittest_settings.py")

    """
    Database initialization and Migration
    """
    db.init_app(app)
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
    app.app_context().push()

    return app
