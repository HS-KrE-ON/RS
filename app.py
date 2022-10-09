"""
Test implementation of a Restful API
"""
import os
from flask import Flask, render_template, request
from static.recommendersystem import input


app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def home():
    """loads home.html file as a template to view"""
    return render_template('index.html')


@app.route('/post', methods=['GET', 'POST'])
def array_post():
    """loads post array"""
    moviearray = request.form.getlist("moviearr[]")
    return {"result": moviearray}


@app.route('/get', methods=['GET', 'POST'])
def get():
    """loads post array"""
    # movies = request.form.getlist('moviearr[]')
    moviearray = ["Koma (2004)", "Lilo and Stitch (2002)"]
    return {"result": input(moviearray)}


if __name__ == '__main__':
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port)
