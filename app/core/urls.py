from flask import Blueprint
from app import app
from app.core.views import LandingPage, UsersPage
bp = Blueprint("/", __name__, url_prefix="/")


app.add_url_rule("/", view_func=LandingPage.as_view("landing_page"))
app.add_url_rule("/users/", view_func=UsersPage.as_view("user"))
