
from movie.movie_entity import *
from theater import *
from rev_entity import *


class RevRepo:
    '''
    아는 것: 영화 정보, 상영 시간, 선택 좌석, id
    하는 것: 예매 정보 저장
    '''

    # 예매 정보 생성 후 리스트 변환
    def rev_make(self, title, time, seat):
        rev_entity = RevEntity(title, time, seat) # 객체 생성
        rev_id = rev_entity.get_rev_id() # id 받기
        reservation = [rev_id, title, time, seat]
        return reservation

    # 예매 정보 저장
    def save_rev(self, reservation, file_name = 'reservations.txt'):
        with open(file_name, 'a', encoding='utf-8') as f:
            reservation_str = ','.join(reservation) # 리스트를 쉼표 기준으로 문자열 변환
            f.write(f'{reservation}\n')
        print(f"{file_name} saved")


# 테스트용 정보
title_1 = '극한직업'
time_1 = '10:00'
seat_1 = '(1, 1)'

# RevRepository 클래스의 인스턴트 생성
repo = RevRepo()

# 예매정보 생성
reservation = repo.rev_make(title_1, time_1, seat_1)
repo.save_rev(reservation)
