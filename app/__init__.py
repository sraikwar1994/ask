import os
from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")
app.config.from_object(os.environ.get("APP_SETTINGS", "config.DevelopmentConfig"))


def register_blueprints(application):
    from app.core import views
    application.register_blueprint(blueprint=views.bp)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


register_blueprints(app)
