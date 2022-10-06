"""
Test implementation of a Restful API
"""
import os
from flask import Flask, render_template, request, url_for
from script import movies

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
    """loads home.html file as a template to view"""
    if request.method == "POST":
        movies = request.form["movie_arr"]
    else:    
        return render_template('index.html')

@app.route("/post", methods = ['GET', 'POST'])
def array_post():
    if request.method == 'POST':
        moviearray = request.form.getlist("movies[]")
    for movie in moviearray:
        print(movie)
    return ""

if __name__=='__main__':
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port)
