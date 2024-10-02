from movie.movie_service import *
from theater.theater_service import *
from admin.admin_service import *
from rev.rev_service import *
from rev.rev_repo import *

movie = MovieService()
theater = TheaterService()
admin = AdminService()
rev = RevService()
rev_repo = RevRepo()



def main_menu():
    while True:
        select = input("1. 영화 예매 2.예매 조회 3. 관리자모드  0.종료 > ")

        match select:
            case "1":
                movie_menu()

            case "2": # 1처럼 부를 수 있게 설정
                check_rev()
            # ---------------------------------------------------------------------------------#
            case "3":
                admin_code = input("관리자코드를 입력해주세요 > ")
                respond = admin.authenticate_admin(admin_code)
                if respond == True:
                    admin_menu()
            case "0":
                return False
            case _:
                print("잘못된 입력입니다. 다시 입력하세요")


# -----------------------------------------------------------------------------------------------------------------------------------#
def movie_menu():
    print(f'----상영 중인 영화----')
    movie_time_list = theater.get_movie_time_list()
    for i in range(len(movie_time_list)):
        print(f'{i + 1}번) {movie_time_list[i][0]}:00 - {movie_time_list[i][1]}')
    while True:
        try:
            time_choice = int(input("영화 상영 시간을 골라주세요 > ")) - 1  # 예외처리
            break
        except ValueError:
            print("-------잘못된 입력입니다. 다시 입력하세요 ------")

    seat = theater.get_seat_list(time_choice)
    for r in range(len(seat)):
        print(" " * len(seat) + str(r), end="")
    print()
    for r in range(len(seat)):
        print(str(r) + ("|" + " " * len(seat)) * len(seat) + "|")

    # seat-check 함수에 choice 넘겨
    while True:
        try:
            x, y = map(int, input("자리를 선택해주세요 ex) 1,1 > ").split(','))  # 예외처리
        except ValueError:
            print("-------잘못된 입력입니다. 다시 입력하세요 ------")

        respond = theater.possible_seat_choice(x, y, time_choice)  ## 차지된 자리면 0 >> 다시 입력 1이면 통과

        if respond == 1:
            pay_check = input("결제를 진행하시겠습니까? (y/n): ").lower()

            if pay_check == "y":
                print("🎫🎫🎫 예매가 완료되었습니다. 🎫🎫🎫")
                time = movie_time_list[time_choice][0]  # => [10,베테랑2]
                title = movie_time_list[time_choice][1]
                seat = [x, y]
                rev_id=rev.rev_make(title,time,seat)
                # 결제가 완료된 후 예매 결과 출력
                print_booking(title, time, seat, rev_id)
                break


            elif pay_check == 'n':
                print("결제를 취소하여 프로그램을 종료합니다.\n🤗 다음에 또 오세요. 🤗")
                break

            else:
                print("잘못된 입력입니다.\n😊 y 또는 n으로 입력해 주세요. > 😊")  # 잘못 입력시 다시 y/n 선택


        else:
            print("이미 차지된 자리입니다.")

        # 1-4, 1-5 넣기
        # 영화 예매 결과 출력
        # import

    return False  # 예매 한번 완료하면 프로그램 종료 !!


# ---------------------------------------------------------------------------------#

def admin_menu(self):
    while True:
        print("\n메뉴를 선택하세요:")
        print("1. 총 매출 및 이윤 확인")
        print("2. 총 관객 수 확인")
        print("3. 종료")

        choice = input("선택: ")
        match choice:
            case '1':
                revenue, profit = admin.calculate_revenue_and_profit()
                print(f"총 매출: {revenue}원, 총 이윤: {profit}원")
            case '2':
                total_audience = admin.total_audience_count()
                print(f"총 관객 수: {total_audience}명")
            case '3':
                print("프로그램을 종료합니다.")
                break
            case _:
                print("잘못된 선택입니다. 다시 시도하세요.")


# ---------------------------------------------------------------------------------#
def print_booking(title, time, seat, rev_id):
            # 선택한 영화 제목
    print(f'[영화제목: {title}]\n[상영시간: {time}]\n[선택좌석: {seat}]\n[예매번호: {rev_id}]')


# ---------------------------------------------------------------------------------#

def check_rev():
    user_rev_id = input("예매번호를 입력하세요 > ")
    reservation=rev_repo.reservations
    if user_rev_id.isdigit():
        found = False # False로 초기화 (없다고 가정)
        for rev in reservation:
            if rev[0] == user_rev_id: # 예매 번호 일치시
                print(f"예매 내역: 영화제목: {rev[1]} , 상영시간: {rev[2]},선택 좌석: {rev[3]}")
                found = True
                break

        if not found: #True
            print("존재하지 않는 예매번호입니다.")

    else :
        print("존재하지 않는 예매번호입니다 > ")


if __name__ == '__main__':
    main_menu()
