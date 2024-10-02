from datetime import datetime

# 현재 날짜 241001 형식
today = datetime.today().strftime('%y%m%d')


class RevEntity:
    rev_count = 1 # 예약 번호 생성 클래스 변수

    def __init__(self,title, time, seat):
        self.today = today
        self.rev_id = f'{self.today}{RevEntity.rev_count}' # 예매 번호 생성
        RevEntity.rev_count += 1 # 예매 번호 증가

    def __repr__(self):
        return f'오늘 날짜: {self.today}, 예매 번호 : {self.rev_id}'

    def get_rev_id(self):
        return self.rev_id

    def get_today(self):
        return self.today

    def get_rev_count(self):
        return self.get_rev_id()

    def set_rev_id(self, new_rev_id):
        self.rev_id = new_rev_id

    def set_today(self, new_today):
        self.today = new_today