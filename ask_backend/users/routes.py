from flask import Blueprint, render_template, request
from flask.views import View
from flask_restful import Resource

from ask_backend.base_models import db
from ask_backend.users.models import User
from ask_backend.users.schema import UserSchema

user_bp = Blueprint("users", __name__)


class UsersPage(View):
    def dispatch_request(self):
        return render_template("pages/core/manage_user.html")


class UserApiView(Resource):
    def get(self, user_id=None):
        if user_id:
            user_schema = UserSchema()
            user = User.query.get(user_id)
            return user_schema.dumps(user)
        else:
            user_schema = UserSchema(many=True)
            users = User.query.all()
            return user_schema.dumps(users)

    def post(self):
        args = request.json
        data = {
            "username": args.get("username"),
            "email": args.get("email"),
            "firstname": args.get("firstname"),
            "lastname": args.get("lastname"),
        }
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return {
            "status": True,
        }, 201

    def put(self):
        args = request.json
        user = User.query.get(args.get("id"))
        if user:
            user.username = args.get("username")
            user.email = args.get("email")
            user.firstname = args.get("firstname")
            user.lastname = args.get("lastname")
            db.session.commit()
            user_schema = UserSchema()
            return user_schema.dumps(user), 200
        else:
            return {"status": False}, 404

    def delete(self):
        args = request.json
        user = User.query.get(args.get("id"))
        if user:
            db.session.delete(user)
            db.session.commit()
            return {"status": True}, 200
        else:
            return {"status": False}, 404


"""
Page Views url rules
"""
user_bp.add_url_rule("/users/", view_func=UsersPage.as_view("users"))

"""
API url rules
"""
user_bp.add_url_rule("/api/users/", view_func=UserApiView.as_view("user_api"))
user_bp.add_url_rule(
    "/api/users/<user_id>", view_func=UserApiView.as_view("get_user_api")
)
user_bp.add_url_rule(
    "/api/users/create/", view_func=UserApiView.as_view("create_user_api")
)
user_bp.add_url_rule(
    "/api/users/delete/", view_func=UserApiView.as_view("delete_user_api")
)
user_bp.add_url_rule(
    "/api/users/update/", view_func=UserApiView.as_view("update_user_api")
)
