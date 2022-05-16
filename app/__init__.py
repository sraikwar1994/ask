import os

from flask import Flask, render_template
from flask_marshmallow import Marshmallow
from flask_restful import Api

app = Flask(__name__, template_folder="templates")
app.config.from_object(os.environ.get("APP_SETTINGS", "config.DevelopmentConfig"))
ma = Marshmallow(app)
api = Api(app)


def register_blueprints(application):
    from app.core.urls import bp as core_bp

    application.register_blueprint(blueprint=core_bp)


def migrate_db(application):
    from flask_migrate import Migrate

    from app.db import db

    db.init_app(application)
    Migrate(application, db)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


register_blueprints(app)
migrate_db(app)
