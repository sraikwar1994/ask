import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="../templates")
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://flask_user:flask_password@localhost:5432/flask_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

import core.views
