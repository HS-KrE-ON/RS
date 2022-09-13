"""Module establishing different website views"""
# pylint: disable=E1101
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.root('/')
def home():
    """loads home.html file as a template to view"""
    return render_template("home")
