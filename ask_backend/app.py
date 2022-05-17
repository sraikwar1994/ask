import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(
    os.environ.get("APP_SETTINGS", "ask_backend.config.DevelopmentConfig")
)
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

"""
Database initialization and Migration
"""
db.init_app(app)
Migrate(app, db)


"""
Register Blueprints
"""
from ask_backend.core.routes import core_bp
from ask_backend.errors.handlers import errors_bp
from ask_backend.users.routes import user_bp

app.register_blueprint(errors_bp)
app.register_blueprint(core_bp)
app.register_blueprint(user_bp)
