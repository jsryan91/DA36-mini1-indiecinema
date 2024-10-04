import os
from movie.movie_entity import *
from theater import *
from rev.rev_entity import *



class RevRepo:
    '''
    아는 것: 영화 정보, 상영 시간, 선택 좌석, id
    하는 것: 예매 정보 저장
    '''
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_name = os.path.join(current_dir, 'reservations.txt')
        self.reservations = []
        self.rev_entity = RevEntity()

        # 파일에서 예매 정보를 읽어 리스트에 저장
        try:
            with open(self.file_name, 'r', encoding = 'utf-8') as f:
                for line in f:
                    # 파일에서 읽은 한 줄을 리스트로 변환하여 저장
                    info=list(line.strip().split(','))
                    self.reservations.append(info)
        except FileNotFoundError:
            print(f"{self.file_name} 파일이 존재하지 않습니다. 새로 생성됩니다.")

    # 총 예매 누적수 반환
    def get_rev_count(self):
        rev_count = len(self.reservations)
        return rev_count

    # 예매번호 생성
    def make_rev_id(self):
        today = self.rev_entity.get_today() # 오늘 날짜
        rev_count = self.get_rev_count()
        rev_id = f'{today}{rev_count + 1}' # 1 증가 후 예매 번호 생성
        return rev_id

    # 예매 정보 생성 후 리스트 변환
    def reservation_info(self, rev):
        rev_id = self.make_rev_id() # id 받기
        reservation = rev_id, rev[0], rev[1], rev[2],rev[3]
        print(reservation)
        self.save_rev(reservation)
        return reservation

    # 예매 정보 저장

    # -----------------------------------------------------------#












    def save_rev(self, reservation):
        self.reservations.append(reservation)
        reservation_str=",".join(map(str,reservation))
        with open(self.file_name, 'a', encoding='utf-8') as f:
            f.write(f'{reservation_str}\n')








    def get_revs(self):
        return self.reservations

    def get_count(self):
        return len(self.reservations)

if __name__ == '__main__':
    r=RevRepo()
    print(r.reservation_info(['1','12','1','1']))