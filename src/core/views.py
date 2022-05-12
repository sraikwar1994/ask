from app import app
from flask import render_template, views

class RenderLandingPageView(views.View):
    
    def dispatch_request(self):
        return render_template('pages/index.html')

app.add_url_rule('/', view_func=RenderLandingPageView.as_view('landing_page'))