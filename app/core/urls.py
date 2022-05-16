from flask import Blueprint

from app import app
from app.core.apis import UserApiView
from app.core.views import LandingPage, UsersPage

bp = Blueprint("/", __name__, url_prefix="/")

"""
Page view urls
"""
app.add_url_rule("/", view_func=LandingPage.as_view("landing_page"))
app.add_url_rule("/users/", view_func=UsersPage.as_view("users"))

"""
API view urls
"""
app.add_url_rule("/api/users/", view_func=UserApiView.as_view("user_api"))
app.add_url_rule("/api/users/<user_id>", view_func=UserApiView.as_view("get_user_api"))
app.add_url_rule("/api/users/create/", view_func=UserApiView.as_view("create_user_api"))
app.add_url_rule("/api/users/delete/", view_func=UserApiView.as_view("delete_user_api"))
app.add_url_rule("/api/users/update/", view_func=UserApiView.as_view("update_user_api"))
