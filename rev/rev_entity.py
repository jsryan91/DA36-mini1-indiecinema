from datetime import datetime

# 현재 날짜 241001 형식
today = datetime.today().strftime('%y%m%d')


class RevEntity:
     # 예약 번호 생성 클래스 변수

    def __init__(self):
        self.today = today
        self.rev_count = 1

    # def __repr__(self):
    #     return f'오늘 날짜: {self.today}'

    def get_today(self):
        return self.today

    def set_today(self, new_today):
        self.today = new_today

    def get_rev_count(self):
        return self.rev_count

    def set_rev_count(self, count):
        self.rev_count = count