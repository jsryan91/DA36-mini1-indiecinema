from theater.theater_repo import *

class TheaterService:
    def __init__(self):
        self.theater_repo = TheaterRepo()

    def get_time_list(self, movie_choice):
        return self.theater_repo.get_time_list(movie_choice)

    def get_seat_list(self, time_choice):
        return self.theater_repo.get_seat_list(time_choice)

    def possible_seat_choice(self, x, y,time_choice):
        return self.theater_repo.possible_seat_choice(x,y,time_choice)