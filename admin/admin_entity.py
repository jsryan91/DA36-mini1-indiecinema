class AdminEntity:
    def __init__(self):
        self.admin_code="admin"
        self.margin_rate=0.4
        self.ticket_price=10_000

    def get_margin_rate(self):
        return self.margin_rate
    def get_ticket_price(self):
        return self.ticket_price

    def set_margin_rate(self,new_rate):
        self.margin_rate=new_rate
    def set_ticket_price(self,new_ticket_price):
        self.ticket_price=new_ticket_price


# get rev_count += 1