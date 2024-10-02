from movie.movie_service import *
from theater.theater_service import *

movie=MovieService()
theater=TheaterService()

def main_menu():
    while True:
        select=input("1. 영화 예매 2.예매 조회 3. 관리자모드  0.종료 > ")

        match select:
            case "1":
#-----------------------------------------------------------------------------------------------------------------------------------# 영화 선택 (movie-entity 참고)
                # 이거 movie_reservation_menu()로 def 빼도 될 듯
                # 영화 list출력 후 >> 영화를 고르게끔 (영화 list 날짜지나면 제거해야함 !!!!! ㅜㅜㅠ ㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜ
                moive_list=movie.get_movie_list()
                for i,info in enumerate(moive_list):
                    print(f'영화{i+1}) {info}')
                while True:
                    try:
                        movie_choice = int(input("영화 번호를 골라주세요 > "))  ## str으로 입력시 error => program 종료 >> try-exception문으로 예외처리 진행해야함
                        break
                    except ValueError:
                        print("-------잘못된 입력입니다. 다시 입력하세요 ------")
#-----------------------------------------------------------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------------------------------------------------------# 상영시간, 좌석 선택 (theater-entity 참고)
            #     ## theater class 구성부터 걍 죽고 싶다 ~~~
            #     # 상영시간 class로 movie_choice를 넘겨주자
                time_list=theater.get_time_list(movie_choice-1)
                # 그럼 상영시간 출력해주고 >> 수정 필요 (일단 시간은 잘 넘겨받음)
                print(f'----{time_list[0][1]}----')
                for i in range(len(time_list)):
                    print(f'{i+1}번) {time_list[i][0]}시')
                while True:
                    try:
                        time_choice=int(input("영화 상영 시간을 골라주세요 > "))-1 # 예외처리
                        break
                    except ValueError:
                        print("-------잘못된 입력입니다. 다시 입력하세요 ------" )
                print(time_choice)


            # 상영시간 정보 넘겨주자 >>그럼 seat return 해줘
                seat=theater.get_seat_list(time_choice)
                # ----------------------------------- 구현미완 -----------------------------------#


                def draw_grid(rows, cols):
                    for r in range(rows):
                        # 격자의 가로선을 그립니다.
                        print("+---" * cols + "+")
                        # 격자의 세로선을 그립니다.
                        print("|   " * cols + "|")
                    # 마지막 가로선을 그립니다.
                    print("+---" * cols + "+")

                # ----------------------------------- 구현미완 -----------------------------------#
               
            
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
