from flask import Blueprint, render_template
from flask.views import MethodView, View

from app import app

bp = Blueprint("/", __name__, url_prefix="/")


class LandingPage(View):
    def dispatch_request(self):
        return render_template("pages/index.html")


class UserAPI(MethodView):
    def get(self, user_id):
        if user_id is None:
            # return a list of users
            pass
        else:
            # expose a single user
            pass

    def post(self):
        # create a new user
        pass

    def delete(self, user_id):
        # delete a single user
        pass

    def put(self, user_id):
        # update a single user
        pass


app.add_url_rule("/", view_func=LandingPage.as_view("landing_page"))
app.add_url_rule("/users", view_func=LandingPage.as_view("user"))
