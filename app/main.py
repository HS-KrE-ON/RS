"""
Test implementation of a Restful API
"""
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """loads home.html file as a template to view"""
    statement = 'Hello Wordl!'
    #render_template('home.html')
    return statement

if __name__=='__main__':
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port)
