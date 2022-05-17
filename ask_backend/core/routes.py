from flask import Blueprint, render_template
from flask.views import View

core_bp = Blueprint("core", __name__)


class LandingPageView(View):
    def dispatch_request(self):
        return render_template("pages/index.html")


core_bp.add_url_rule("/", view_func=LandingPageView.as_view("landing_page"))
