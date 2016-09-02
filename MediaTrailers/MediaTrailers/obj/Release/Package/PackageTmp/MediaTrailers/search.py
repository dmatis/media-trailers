import urllib2
import re
import requests
import json
import urllib


def get_youtube_trailer(movie):
    """Gets the first link from a youtube search for a given movie trailer"""
    query_string = movie + " trailer"
    query_string.replace(" ", "%20")
    results = requests.get('http://www.youtube.com/results', params={'search_query':query_string})
    
    results.encoding = 'ISO-8859-1'
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', results.text)
    return "http://www.youtube.com/watch?v=" + search_results[0]

def get_poster(id):
    """Gets the poster url from a given IMDB id"""
    prefix_uri = "http://image.tmdb.org/t/p/original/"
    poster_uri = get_poster_path(id)
    print poster_uri
    return prefix_uri + poster_uri

def get_poster_path(id):
    print id
    data = json.loads(urllib.urlopen("https://api.themoviedb.org/3/movie/"+id+"?api_key=323e42cf02dc78b90a260de2d7f3ae0c").read())
    return data["poster_path"]