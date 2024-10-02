from movie.movie_repo import *

class MovieService:
    def __init__(self):
        self.movie_repo=MovieRepo()

    def get_movie_list(self):
        return self.movie_repo.get_movie_list()