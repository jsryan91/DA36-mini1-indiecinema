# main #4 관리자 + admin Class 짜기

# 관리자 여부 확인

# Constants
TICKET_PRICE = 10000  # 티켓 가격은 10,000원
MARGIN_RATE = 0.40    # 마진율 40%
ADMIN_ID = "admin"    # 관리자 아이디

def authenticate_admin():
    """
    관리자 아이디를 입력받아 인증하는 함수.
    
    Returns:
    bool: 올바른 관리자 아이디일 경우 True, 아닐 경우 False
    """
    admin_id = input("관리자 아이디를 입력하세요: ")
    if admin_id == ADMIN_ID:
        return True
    else:
        print("잘못된 관리자 아이디입니다. 프로그램을 종료합니다.")
        return False

def calculate_revenue_and_profit(audience_count):
    """
    관객 수를 기반으로 총 매출과 이윤을 계산하는 함수.
    
    Parameters:
    audience_count (int): 관객 수
    
    Returns:
    tuple: 매출과 이윤 (revenue, profit)
    """
    revenue = TICKET_PRICE * audience_count
    profit = revenue * MARGIN_RATE
    return revenue, profit

def show_total_revenue_and_profit():
    """
    관객 수를 입력받아 총 매출과 이윤을 출력하는 함수.
    """
    try:
        audience_count = int(input("관객 수를 입력하세요: "))
        if audience_count < 0:
            print("관객 수는 음수가 될 수 없습니다.")
            return
    except ValueError:
        print("유효한 숫자를 입력하세요.")
        return
    
    revenue, profit = calculate_revenue_and_profit(audience_count)
    print(f"총 매출: {revenue}원")
    print(f"총 이윤: {profit}원")

def show_audience_count():
    """
    관객 수를 입력받아 출력하는 함수.
    """
    try:
        audience_count = int(input("관객 수를 입력하세요: "))
        if audience_count < 0:
            print("관객 수는 음수가 될 수 없습니다.")
            return
        print(f"총 관객 수: {audience_count}명")
    except ValueError:
        print("유효한 숫자를 입력하세요.")

def admin_panel():
    """
    관리자 메뉴를 표시하는 함수. 인증 후 메뉴를 선택할 수 있음.
    """
    if not authenticate_admin():
        return  # 인증 실패 시 종료
    
    print("\n관리자 메뉴:")
    print("1. 총 매출과 이윤 확인")
    print("2. 관객 수 확인")
    
    try:
        choice = int(input("메뉴를 선택하세요 (1 또는 2): "))
        if choice == 1:
            show_total_revenue_and_profit()
        elif choice == 2:
            show_audience_count()
        else:
            print("잘못된 선택입니다.")
    except ValueError:
        print("유효한 숫자를 입력하세요.")

# 관리자 메뉴 실행
admin_panel()




