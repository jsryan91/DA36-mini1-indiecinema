class Movie:
    def __init__(self,title,period):
        self.title=title
        self.period=period

    def get_title(self):
        return self.title
    def get_period(self):
        return self.period

    def set_title(self,title):
        self.title=title
    def set_period(self,period):
        self.period=period

    def __repr__(self):
        return f'영화 제목 : {self.title}, 상영 기간 : {self.period}'
