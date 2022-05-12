from flask import Flask, render_template, template_rendered
app = Flask(__name__, template_folder='../templates')
import core.views