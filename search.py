import urllib2
import re
import requests

def get_youtube_trailer(movie):
    """Gets the first link from a youtube search for a given movie trailer"""
    query_string = movie + " trailer"
    query_string.replace(" ", "%20")
    results = requests.get('http://www.youtube.com/results', params={'search_query':query_string})
    
    results.encoding = 'ISO-8859-1'
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', results.text)
    return "http://www.youtube.com/watch?v=" + search_results[0]
