import datetime, os

class EventRepo:
    def __init__(self):
        self.event_list = []
        self.date = datetime.datetime.now().strftime('%y%m%d')

        current_dir = os.path.dirname(os.path.abspath(__file__))
        event_file_path = os.path.join(current_dir, 'event.txt')

        # 파일에서 이벤트 목록 불러오기
        with open(event_file_path, 'r',encoding='utf-8') as f:
            text_line=f.readlines()
            for line in text_line:
                line=line.strip().split(",")
                if int(line[2]) >= int(self.date):
                    self.event_list.append(line)


    def get_event_list(self):
        return self.event_list

    # 영화 제목에 따라 이벤트 반환
    def get_event_by_title(self, title):
        for movie_event in self.event_list:
            if movie_event[0] == title:
                return movie_event[1] # 이벤트 내용 반환
        return None # 해당 영화에 대한 이벤트 없는 경우
