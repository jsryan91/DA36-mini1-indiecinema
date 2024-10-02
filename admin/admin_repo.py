from admin.admin_entity import *
from rev import rev_repo

class AdminRepo:
    def __init__(self, admin_code):
        self.admin_code = admin_code

    def authenticate_admin(self):
            """
            관리자 아이디를 입력받아 인증하는 함수.

            Returns: 올바른 관리자 아이디일 경우 True, 아닐 경우 False
            """
            admin_id = input("관리자 아이디를 입력하세요: ")
            if admin_id == self.admin_code:
                return True
            else:
                print("잘못된 관리자 아이디입니다. 프로그램을 종료합니다.")
                return False

    def calculate_revenue_and_profit(self, admin):
        """
        총 매출과 총 이윤을 계산하는 함수.
        """
        total_revenue = admin.get_ticket_price() * admin.get_count()
        total_profit = total_revenue * admin.get_margin_rate()
        return total_revenue, total_profit

    def total_audience_count(self):
        """
        rev_repo 에서 관객 수를 입력받아 출력하는 함수.
        #TODO: 관객수 rev 에서 가져오기
        """
        pass

    def admin_menu(self, admin):
        while True:
            print("\n메뉴를 선택하세요:")
            print("1. 총 매출 및 이윤 확인")
            print("2. 총 관객 수 확인")
            print("3. 종료")

            choice = input("선택: ")

            if choice == '1':
                revenue, profit = self.calculate_revenue_and_profit(admin)
                print(f"총 매출: {revenue}원, 총 이윤: {profit}원")
            elif choice == '2':
                total_audience = admin.get_count()
                print(f"총 관객 수: {total_audience}명")
            elif choice == '3':
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 선택입니다. 다시 시도하세요.")

# 예시
admin = Admin(count=100)  # 판매량 100으로 Admin 인스턴스 생성
admin_repo = AdminRepo("admin")

if admin_repo.authenticate_admin():
    admin_repo.admin_menu(admin)
else:
    print("인증 실패!")

