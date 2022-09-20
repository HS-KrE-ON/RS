"""
Test implementation of a Restful API
"""
import os
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Hello():
    """loads .html file as a template to view"""
    df = pd.read_csv("https://raw.githubusercontent.com/HS-KrE-ON/RS/main/archive/movie_titles.csv",
                 encoding = "ISO-8859-1", on_bad_lines='skip')
    return df.to_html()

@app.route('/home')
def Home():
    """loads home.html file as a template to view"""
    return render_template('base.html')

if __name__=='__main__':
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port)
