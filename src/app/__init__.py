import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="../templates")
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)

import core.views
