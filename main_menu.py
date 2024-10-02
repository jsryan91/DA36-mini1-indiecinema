def rev_content_print():
    print("ijdnfskajfisokal")
# mainmenu 기능명세 1-5)


while True:
    select=input("1. 영화 예매 2.예매 조회 3. 관리자모드  0.종료")

    match select:
        case "1":
            pass
        case "2":
            rev_id=input("예매번호를 입력하세요 > ")

        case "3":
            admin_password=input("관리자 코드를 입력하세요 > ")
        case "0":
            pass
        case _:
            print("잘못된 입력입니다. 다시 입력하세요")