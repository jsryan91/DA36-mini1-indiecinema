from rev.rev_repo import *

class RevService:
    def __init__(self):
        self.rev_repo=RevRepo() # RevRepo 인스턴스 생성

    def rev_make(self, rev):
        return self.rev_repo.rev_make(rev)  # 예매 정보 생성

    def save_rev(self,rev_id, reservation):
        self.rev_repo.save_rev(rev_id, reservation)  # 예매 정보 저장

