__author__ = 'Darren Matis'

from flask import Flask, request
import entertainment_center
import json
import urllib

app = Flask(__name__)

@app.route('/')
def index_page():
    return entertainment_center.get_movies()

@app.route('/get_imdb', methods=['GET', 'POST'])
def hello_world():
    data = json.loads(urllib.urlopen("http://www.omdbapi.com/?t="+request.form['movie-title']).read())
    if data["Response"] == "True":
        entertainment_center.add_movie(data)
    return entertainment_center.get_movies()

if __name__ == '__main__':
    app.run()
