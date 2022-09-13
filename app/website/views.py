# pylint: disable=E1101
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.root('/')
def home():
    # loads the home.html file in to the view
    return render_template("home")
