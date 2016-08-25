import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "http://moviecultists.com/wp-content/uploads/2009/11/avatar-poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_matrix = media.Movie("The Matrix",
                        "He chose the red pill",
                        "https://www.movieposter.com/posters/archive/main/9/A70-4902",
                        "https://www.youtube.com/watch?v=m8e-FF8MsqU")

movies = [toy_story, avatar, the_matrix]
fresh_tomatoes.open_movies_page(movies)
