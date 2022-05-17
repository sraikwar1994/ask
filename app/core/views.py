from flask import blueprints, render_template
from flask.views import View

from app import app


class LandingPage(View):
    def dispatch_request(self):
        return render_template("pages/index.html")


class UsersPage(View):
    def dispatch_request(self):
        return render_template("pages/core/manage_user.html")
