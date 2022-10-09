"""
Test implementation of a Restful API
"""
import os
from flask import Flask, render_template, request, jsonify
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
    results = recommendate(movies)
    return results


@app.route('/get', methods=['GET', 'POST'])
def get():
    """loads post array"""
    # movies = request.form.getlist('moviearr[]')
    moviearray = ["Dinosaur Planet (2003)"]
    return recommendate(moviearray)


if __name__ == '__main__':
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port)
