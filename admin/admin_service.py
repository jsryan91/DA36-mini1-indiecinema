from admin.admin_repo import *

class AdminService:
    def __init__(self):
        self.admin_repo = admin_repo

    def authenticate_admin(self):
        return self.admin_repo.authenticate_admin()

    def calculate_revenue_and_profit(self):
        return self.admin_repo.calculate_revenue_and_profit()

    def total_audience_count(self):
        return self.admin_repo.total_audience_count()
