"""
Test implementation of a Restful API
"""
import os
from flask import Flask, render_template, request
from static.recommendersystem import recommendate


app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def home():
    """loads home.html file as a template to view"""
    return render_template('index.html')


@app.route('/post', methods=['GET', 'POST'])
def array_post():
    """loads post array"""
    movies = request.form.getlist('moviearr[]')
    return recommendate(movies)

if __name__ == '__main__':
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port)
