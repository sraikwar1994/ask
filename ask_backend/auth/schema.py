from ask_backend.app import ma


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "firstname", "lastname", "username", "email")
