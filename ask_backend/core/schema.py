from flask_marshmallow import Marshmallow

from ask_backend import app

ma = Marshmallow(app)


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "firstname", "lastname", "username", "email")
