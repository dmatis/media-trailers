import media
import json
import os
import search
from MediaTrailers import fresh_tomatoes


def add_movie(data):
    json_data = ""
    entry = {'title': data["Title"], 'year': data["Year"], 'plot': data["Plot"], 'poster': search.get_poster(data["imdbID"]), 'trailer': search.get_youtube_trailer(data["Title"]), 'imdb_id': data["imdbID"]}
    with open('MediaTrailers/media.json', 'r') as f:
        json_data = json.load(f)
    
    if not any (entry['title'] == d['title'] for d in json_data['movies']):
        with open('MediaTrailers/media.json', 'w') as json_output:
            json_data['movies'].append(entry)
            json.dump(json_data, json_output)

def get_movies():
    movies = []
    print os.getcwd()
    with open('MediaTrailers/media.json') as json_data:
        json_obj = json.load(json_data)
        for i in json_obj['movies']:
            curr_movie = media.Movie(i['title'],i['year'],i['plot'],i['poster'],i['trailer'], i['imdb_id'])
            movies.append(curr_movie)
    return fresh_tomatoes.open_movies_page(movies)

