from flask import Blueprint

from app import app
from app.core.apis import UserApiView
from app.core.views import LandingPage, UsersPage

core_bp = Blueprint("/", __name__)

"""
Page view urls
"""
app.add_url_rule(
    "/", "landing_page", LandingPage.as_view("landing_page"), methods=["GET"]
)
app.add_url_rule("/users/", "users", UsersPage.as_view("users"))

"""
API view urls
"""
app.add_url_rule("/api/users/", view_func=UserApiView.as_view("user_api"))
app.add_url_rule("/api/users/<user_id>", view_func=UserApiView.as_view("get_user_api"))
app.add_url_rule("/api/users/create/", view_func=UserApiView.as_view("create_user_api"))
app.add_url_rule("/api/users/delete/", view_func=UserApiView.as_view("delete_user_api"))
app.add_url_rule("/api/users/update/", view_func=UserApiView.as_view("update_user_api"))
