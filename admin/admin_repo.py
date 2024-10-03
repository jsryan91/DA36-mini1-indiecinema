from admin.admin_entity import *
from rev.rev_entity import *

class AdminRepo:
    def __init__(self):
        self.rev_entity=RevEntity()
        self.admin_entity=AdminEntity()

    def authenticate_admin(self,admin_code):
            """
            관리자 아이디를 입력받아 인증하는 함수.
            Returns: 올바른 관리자 아이디일 경우 True, 아닐 경우 False
            """

            if admin_code == self.admin_entity.get_admin_code():
                return True
            else:
                return False

    def calculate_revenue_and_profit(self):
        """
        총 매출과 총 이윤을 계산하는 함수.
        """
        count=self.total_audience_count()
        total_revenue = self.admin_entity.get_ticket_price() *count
        total_profit = total_revenue * self.admin_entity.get_margin_rate()
        return total_revenue, total_profit

    def total_audience_count(self): #rev_repo 에서 관객 수를 입력받아 출력하는 함수.
        count=self.rev_entity.get_rev_count()
        return count




