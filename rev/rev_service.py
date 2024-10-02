from rev.rev_repo import *

class RevService:
    def __init__(self):
        self.rev_repo=RevRepo() # RevRepo 인스턴스 생성

    def rev_make(self, title, time, seat):
        return self.rev_repo.rev_make(title, time, seat)  # 예매 정보 생성

    def save_rev(self, reservation, file_name='reservations.txt'):
        self.rev_repo.save_rev(reservation, file_name)  # 예매 정보 저장

