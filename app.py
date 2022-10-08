"""
Test implementation of a Restful API
"""
import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def home():
    """loads home.html file as a template to view"""
    return render_template('index.html')


@app.route("/post1", methods=['GET', 'POST'])
def array_post():
    """loads post array"""
    if request.method == 'POST':
        moviearray = request.form.getlist("movies[]")
    return moviearray


@app.route("/post", methods=['GET', 'POST'])
def post():
    """loads post array"""
    movies = request.form.getlist("moviearray[]")
    text = movies.toString()
    return render_template('post.html')


if __name__ == '__main__':
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port)
