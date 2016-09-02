"""
Routes and views for the flask application.
"""
__author__ = 'Darren Matis'

from flask import Flask, request
from MediaTrailers import entertainment_center
import json
import urllib
from datetime import datetime
from flask import render_template
from MediaTrailers import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return entertainment_center.get_movies()

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/get_imdb', methods=['GET', 'POST'])
def get_imdb_data():
    data = json.loads(urllib.urlopen("http://www.omdbapi.com/?t="+request.form['movie-title']).read())
    if data["Response"] == "True":
        entertainment_center.add_movie(data)
    return entertainment_center.get_movies()

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
