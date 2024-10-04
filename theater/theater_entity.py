class Theater:
    def __init__(self):
        self.time_list=[10,12,14,16,18,20]

        self.time_seat_dic={}
        for i in range(len(self.time_list)):
            self.time_seat_dic[self.time_list[i]]=[[0,0,0],[0,0,0],[0,0,0]]


    def get_time_list(self):
        return list(self.time_seat_dic.keys())

    def get_seat_list(self):
        return list(self.time_seat_dic.values())

