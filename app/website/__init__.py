"""Module initialising the website using flask"""
from flask import Flask
from .views import views

def create_app():
    """Creates an application using flask with views."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'khshdsjkdf jsdfjuds'

    app.register_blueprint(views, url_prefix='/')

    return app
