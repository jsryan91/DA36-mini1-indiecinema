from movie.movie_service import *
from theater.theater_service import *
from admin.admin_service import *
from rev.rev_service import *
from event.event_service import *


movie_service=MovieService()
theater_service=TheaterService()
admin_service=AdminService()
rev_service=RevService()
event_service=EventService()


#-----------------------------------------------------------------------------------------------------------------------------------#
def main_menu():
    while True:
        select=input("1. 영화 예매 2. 예매 조회 3.전체 이벤트 4. 관리자모드  0.종료 > ")

        match select:
            case "1":
                movie_menu()
                break

            case "2":
                check_rev()

            case "3":
                event_menu()

            case "4":
                admin_code = input("관리자코드를 입력해주세요 > ")
                respond = admin_service.authenticate_admin(admin_code)
                if respond == True:
                    admin_menu()
                    break
                else:
                    print("관리자 코드가 아닙니다.")
            case "0":
                return False
            case _:
                print("잘못된 입력입니다. 다시 입력하세요")
#-----------------------------------------------------------------------------------------------------------------------------------#
def movie_menu():
    print(f'----상영 중인 영화----')
    title_time_list = theater_service.get_movie_time_list()
    respond_list = theater_service.is_seat_full()

    for i in range(len(title_time_list)):
        if respond_list[i]==0:
            print(f'{i + 1}번) {title_time_list[i][0]}:00 - {title_time_list[i][1]}')
        else:
            print(f'{i + 1}번) {title_time_list[i][0]}:00 - {title_time_list[i][1]} -- (매진입니다)')

    while True:
        try:
            time_choice = int(input("영화 상영 시간을 골라주세요 > ")) - 1  # 예외처리
            if respond_list[time_choice] == 0:
                seat = theater_service.get_movie_seat_list(time_choice)
                movie_event = event_service.get_event_by_title(title_time_list[time_choice][1])

                if movie_event == None:
                    print("진행 중인 이벤트가 없습니다.")
                else:
                    print(f'진행 중인 이벤트는{movie_event}입니다.')
                print()
                break
            else:
                print("매진이라니까요")

        except ValueError:
            print("------ 잘못된 입력입니다. 다시 입력하세요 ------")
        except IndexError:
            print("------올바른 영화 번호가 아닙니다. 다시 입력하세요------")


# 좌석 사각형으로 출력하는 코드 # --> 좌석별 o.x 표시하는거 구현할 수 있는지 확인
    for r in range(len(seat)):
        print(" " * len(seat) + str(r), end="")
    print()
    for r in range(len(seat)):
        print(str(r) + ("|" + " " * len(seat)) * len(seat) + "|")

    # seat-check 함수에 choice 넘겨
    while True:
        try:
            x, y = map(int, input("자리를 선택해주세요 ex) 1,1 > ").split(','))  # 예외처리
            respond = theater_service.is_seat_empty(x, y, time_choice)  ## 차지된 자리면 0 >> 다시 입력 1이면 통과
            if respond == 1:
                print(f'선택하신 자리는 {x},{y}입니다.')
                pay_check(x, y, time_choice, title_time_list, movie_event)
                break
            else:
                print("이미 차지된 자리입니다.")
        except ValueError:
            print("-------잘못된 입력입니다. 다시 입력하세요 ------")
        except IndexError:
            print("-- 그런 자리는 없습니다. --")
# ---------------------------------------------------------------------------------#
def admin_menu():
    while True:
        print("\n메뉴를 선택하세요:")
        print("1. 총 매출 및 이윤 확인")
        print("2. 총 관객 수 확인")
        print("3. 종료")

        choice = input("선택: ")
        match choice:
            case '1':
                revenue, profit = admin_service.calculate_revenue_and_profit()
                print(f"총 매출: {revenue}원, 총 이윤: {profit}원")
            case'2':
                total_audience = admin_service.total_audience_count()
                print(f"총 관객 수: {total_audience}명")
            case '3':
                print("관리자 모드를   종료합니다.")
                break
            case _:
                print("잘못된 선택입니다. 다시 시도하세요.")
# ---------------------------------------------------------------------------------#
def check_rev():
    count=0
    user_rev_id = input("예매번호를 입력하세요 > ")
    reservation=rev_service.get_revs()
    event_list = event_service.get_event_list()

    for rev in reservation:
        if rev[0] == user_rev_id: # 예매 번호 일치시
            count=1
            break
    if count==1:
        for event in event_list:
           if event[0]==rev[1]:
                print(f"예매 내역: 영화제목: {rev[1]}, 상영시간: {rev[2]}, 선택 좌석: [{rev[3]},{rev[4]}], 이벤트명: {event[1]}")
           else:
               print(f"예매 내역: 영화제목: {rev[1]}, 상영시간: {rev[2]}, 선택 좌석: [{rev[3]},{rev[4]}],진행중인 이벤트가 없습니다.")
    else:
        print("예매 내역이 없습니다.")

# ---------------------------------------------------------------------------------#

def event_menu():
    print(f'--------진행 중인 이벤트---------')
    event_list = event_service.get_event_list()
    for i in range(len(event_list)):
        print(f'{i + 1}번 영화제목: {event_list[i][0]}, 이벤트:{event_list[i][1]}, 이벤트 기간:{event_list[i][2]}')

# ---------------------------------------------------------------------------------#
def print_booking(reservation, movie_event):
            # 선택한 영화 제목
    print('------------ 선택하신 영화 ----------')
    if movie_event==None:
        print(f'[영화제목: {reservation[1]}]\n[상영시간: {reservation[2]}:00]\n[선택좌석: [{reservation[3]},{reservation[4]}]]\n[예매번호: {reservation[0]}]')
        print("진행 중인 이벤트가 없습니다.")
    else:
        print(f'[영화제목: {reservation[1]}]\n[상영시간: {reservation[2]}:00]\n[선택좌석: [{reservation[3]},{reservation[4]}]]\n[예매번호: {reservation[0]}]\n[이벤트명: {movie_event}]')
# ---------------------------------------------------------------------------------#
def pay_check(x,y,time_choice,movie_time_list, movie_event):
    while True:
        pay_check = input("결제를 진행하시겠습니까? (y/n): ").lower()

        if pay_check == "y":
            print("🎫🎫🎫 예매가 완료되었습니다. 🎫🎫🎫")

            temp_reser=[movie_time_list[time_choice][1], movie_time_list[time_choice][0],x,y]
            reservation=rev_service.reservation_info(temp_reser)
            print_booking(reservation, movie_event)
            theater_service.set_seat_sold(x, y, time_choice)
            break

        elif pay_check == 'n':
            print("결제를 취소하여 프로그램을 종료합니다.\n🤗 다음에 또 오세요. 🤗")
            break

        else:
            print("잘못된 입력입니다.\n😊 y 또는 n으로 입력해 주세요. 😊")  # 잘못 입력시 다시 y/n 선택
#-----------------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    main_menu()





