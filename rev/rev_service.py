from rev.rev_repo import *

class RevService:
    def __init__(self):
        self.rev_repo=RevRepo() # RevRepo 인스턴스 생성

    def make_rev_id(self):
        return self.rev_repo.make_rev_id()










#-----------------------------------------------------------#

    def reservation_info(self, rev):
        return self.rev_repo.reservation_info(rev)  # 예매 정보 생성

    def save_rev(self, reservation):
        self.rev_repo.save_rev(reservation)  # 예매 정보 저장

    def get_revs(self):
        return  self.rev_repo.get_revs()

