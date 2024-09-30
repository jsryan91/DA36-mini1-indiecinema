class Admin:
    def __init__(self,count):
        self.admin_code="admin"
        self.margin_rate=0.4
        self.count=count
        self.ticket_price=10_000

    def __repr__(self):
        return f'마진율: {self.margin_rate}, 판매량 : {self.count}, 티켓 값: {self.ticket_price}'

    def get_margin_rate(self):
        return self.margin_rate
    def get_count(self):
        return self.count
    def get_ticket_price(self):
        return self.ticket_price

    def set_margin_rate(self,new_rate):
        self.margin_rate=new_rate

    def set_count(self,new_count):
        self.count=new_count

    def set_ticket_price(self,new_ticket_price):
        self.ticket_price=new_ticket_price
