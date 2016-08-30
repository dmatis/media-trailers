import webbrowser

class Movie():
    """This class provides information to store related movie information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]    
    
    def __init__(self, movie_title, year, storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.year = year
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        return 'Ok'
