
from movie.movie_entity import *
from theater import *
from rev.rev_entity import *


class RevRepo:
    '''
    아는 것: 영화 정보, 상영 시간, 선택 좌석, id
    하는 것: 예매 정보 저장
    '''
    def __init__(self):
        file_name = 'reservations.txt'
        self.file_name = file_name
        self.reservations = []

        # 파일에서 예매 정보를 읽어 리스트에 저장
        try:
            with open(file_name, 'r', encoding = 'utf-8') as f:
                for line in f:
                    # 파일에서 읽은 한 줄을 리스트로 변환하여 저장
                    self.reservations.append(line.strip().split(', '))
        except FileNotFoundError:
            print(f"{file_name} 파일이 존재하지 않습니다. 새로 생성됩니다.")


    # 예매 정보 생성 후 리스트 변환
    def rev_make(self, title, time, seat):
        rev_entity = RevEntity() # 객체 생성
        rev_id = rev_entity.get_rev_id() # id 받기
        reservation = [rev_id, title, time, seat]
        self.save_rev(reservation)
        return rev_id

    # 예매 정보 저장
    def save_rev(self, reservation):
        self.reservations.append(reservation)
        with open(self.file_name, 'a', encoding='utf-8') as f:
            reservation_str = ','.join(reservation) # 리스트를 쉼표 기준으로 문자열 변환
            f.write(f'{reservation_str}\n')
        print(f"{self.file_name} 저장 완료")



# --------------------------------------------------------------------------------

# 테스트용 정보
title_1 = '극한직업'
time_1 = '10:00'
seat_1 = '(1, 1)'

# RevRepository 클래스의 인스턴트 생성
repo = RevRepo()

# 예매정보 생성
reservation = repo.rev_make(title_1, time_1, seat_1)
repo.save_rev(reservation)
