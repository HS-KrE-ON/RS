"""
Test implementation of a Restful API
"""
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    """loads .html file as a template to view"""
    statement = "hello world!"
    return statement

@app.route('/home')
def home():
    """loads home.html file as a template to view"""
    return render_template('base.html')

if __name__=='__main__':
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port)
