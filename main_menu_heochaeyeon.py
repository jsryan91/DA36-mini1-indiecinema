from movie.movie_service import *
from theater.theater_service import *

movie=MovieService()
theater=TheaterService()

def main_menu():
    while True:
        select=input("1. 영화 예매 2.예매 조회 3. 관리자모드  0.종료 > ")

        match select:
            case "1":

                print(f'----상영 중인 영화----')
                movie_time_list=theater.get_movie_time_list()
                for i in range(len(movie_time_list)):
                    print(f'{i+1}번) {movie_time_list[i][0]}:00 - {movie_time_list[i][1]}')
                while True:
                    try:
                        time_choice=int(input("영화 상영 시간을 골라주세요 > "))-1 # 예외처리
                        break
                    except ValueError:
                        print("-------잘못된 입력입니다. 다시 입력하세요 ------")

                seat=theater.get_seat_list(time_choice)
                for r in range(len(seat)):
                    print(" "*len(seat)+str(r) ,end="")
                print()
                for r in range(len(seat)):
                    print(str(r)+("|"+" "*len(seat) )* len(seat) + "|")


            # seat-check 함수에 choice 넘겨
                while True:
                    try:
                        x, y = map(int, input("자리를 선택해주세요 ex) 1,1 > ").split(','))  # 예외처리
                    except ValueError:
                        print("-------잘못된 입력입니다. 다시 입력하세요 ------")

                    respond=theater.possible_seat_choice(x,y,time_choice) ## 차지된 자리면 0 >> 다시 입력 1이면 통과

                    if respond==1:
                        print("예약이 완료되었습니다.")
                        break
                    else:
                        print("이미 차지된 자리입니다.")


                return False # 예매 한번 완료하면 프로그램 종료 !!
#-----------------------------------------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------#
            case "0":
                return False
            case _:
                print("잘못된 입력입니다. 다시 입력하세요")



if __name__ == '__main__':
    main_menu()
