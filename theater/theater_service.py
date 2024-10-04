from theater.theater_repo import *

class TheaterService:
    def __init__(self):
        self.theater_repo = TheaterRepo()

    def get_movie_time_list(self):
        return self.theater_repo.get_movie_time_list()

    def get_movie_seat_list(self, time_choice):
        return self.theater_repo.get_movie_seat_list(time_choice)

    def is_seat_empty(self, x, y,time_choice):
        return self.theater_repo.is_seat_empty(x,y,time_choice)

    def set_seat(self,x,y,time_choice):
        return self.theater_repo.set_seat(x,y,time_choice)

    def is_seat_full(self):
        return self.theater_repo.is_seat_full()