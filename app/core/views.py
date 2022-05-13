from flask import render_template, Blueprint
from .models import User

bp = Blueprint('/', __name__, url_prefix='/')


@bp.route(rule='/', methods=('GET',))
def get():
    users = User.query.all()
    return render_template('pages/index.html', users=users)


