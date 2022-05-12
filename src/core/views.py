from re import U
from app import app
from flask import render_template, views
from .models import User


class RenderLandingPageView(views.View):
    
    def dispatch_request(self):
        users = User.query.all()
        return render_template('pages/index.html', users=users)

app.add_url_rule('/', view_func=RenderLandingPageView.as_view('landing_page'))