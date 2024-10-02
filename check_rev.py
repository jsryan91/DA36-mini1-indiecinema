
user_rev_id = input("예매번호를 입력하세요 > ")

if user_rev_id.isdigit():
    found = False # False로 초기화 (없다고 가정)
    for rev in rev_repo:
        if rev[0] == user_rev_id: # 예매 번호 일치시
            print(f"예매 내역: {rev[1]}")
            found = True
            break

    if not found: #True
        print("존재하지 않는 예매번호입니다.")

else :
    print("존재하지 않는 예매번호입니다 > ")
