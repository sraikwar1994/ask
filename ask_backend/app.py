import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(
    os.environ.get("APP_SETTINGS", "ask_backend.config.DevelopmentConfig")
)
ma = Marshmallow(app)
api = Api(app)

"""
Database initialization and Migration
"""
from ask_backend.base_models import db

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
