import os

from flask import Blueprint, Flask, render_template
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")
app.config.from_object(os.environ.get("APP_SETTINGS", "config.DevelopmentConfig"))
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

"""
Database initialization and Migration
"""
db.init_app(app)
Migrate(app, db)

"""
blueprint registered
"""
from app.core.urls import core_bp

app.register_blueprint(core_bp)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404
