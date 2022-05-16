from flask import jsonify
from flask_restful import Resource, reqparse

from app.core.models import User
from app.core.schema import UserSchema
from app.db import db


class UserApiView(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("id", type=str, help="UserId", location="json")
    parser.add_argument("username", type=str, help="Username", location="json")
    parser.add_argument("email", type=str, help="Email", location="json")
    parser.add_argument("firstname", type=str, help="Firstname", location="json")
    parser.add_argument("lastname", type=str, help="Lastname", location="json")

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
        args = self.parser.parse_args()
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
        args = self.parser.parse_args()
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
        args = self.parser.parse_args()
        user = User.query.get(args.get("id"))
        if user:
            db.session.delete(user)
            db.session.commit()
            return {"status": True}, 200
        else:
            return {"status": False}, 404
