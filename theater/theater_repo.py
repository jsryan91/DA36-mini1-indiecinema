from theater.theater_entity import *
import random
import datetime
import openpyxl as op
from movie.movie_repo import *

class TheaterRepo:
    def __init__(self):
        self.path="C:/Workspaces/DA36-mini1-indiecinema/theater/theater.xlsx"
        self.date = datetime.datetime.now().strftime('%y%m%d') # excel-sheet를 date로 만들거임 !!
        self.movie_time_list = []
        #---MovieRepo에서 movie_list 가지고 오기-----------#
        self.movie_repo=MovieRepo()
        self.movie_list=self.movie_repo.get_movie_list()
        self.movie_name_list=[self.movie_list[i][0] for i in range(len(self.movie_list))]
        #--------------------------------------------------#
        #---TheaterEntity에서 상영시간(time_list), 좌석(seat_list) 가지고 오기---#
        self.theater_entity=Theater()
        self.time_list=self.theater_entity.get_time_list()
        self.seat_list = self.theater_entity.get_seat_list()
#---------------------------------------------------------------------------------------------------#
 ## .xlsx wb 만들고 sheet 생성
    def open_xlsx(self):

        try:
            self.wb = op.load_workbook(self.path)
        except:
            self.wb = op.Workbook()
            self.wb.save(self.path)
        sheet=str(self.date)

        if sheet not in self.wb.sheetnames:
            self.wb.create_sheet(title=sheet)
            self.wb.save(self.path)
            self.ws=self.wb[sheet]
            self.movie_time_list = [[time, random.choice(self.movie_name_list)] for time in self.time_list]

            for i in range(len(self.time_list)):
                seat = self.seat_list[i]
                cell=self.ws.cell(row=1+i*len(seat),column=1)
                cell.value="/".join(map(str,self.movie_time_list[i]))

                for j in range(len(seat)):
                    for p in range(len(seat[0])):
                        cell=self.ws.cell(row=i*len(seat)+j+1,column=p+2)
                        cell.value=seat[j][p]
        else:
            for i in range(len(self.time_list)):
                self.ws=self.wb[sheet]
                cell=self.ws.cell(row=1+i*len(self.seat_list[i][1]),column=1)
                if cell.value is not None:
                    self.movie_time_list.append(list(cell.value.split("/")))
        self.wb.save(self.path)

#---------------------------------------------------------------------------------------------------#

    def get_movie_time_list(self): # 영화 및 상영시간 return
        self.open_xlsx()
        return self.movie_time_list

#---------------------------------------------------------------------------------------------------#

    def get_seat_list(self,time_choice): # 영화 상영시간 별 좌석 return
        seat=self.seat_list[time_choice]
        for i in range(len(seat)):
            for j in range(len(seat[0])):
                cell = self.ws.cell(row=1+i+len(seat)*time_choice, column= j + 2)
                seat[i][j]=cell.value
        return self.seat_list[time_choice]

#---------------------------------------------------------------------------------------------------#

    def possible_seat_choice(self, x, y,time_choice): # 고른자리가 구매가능한지 확인하기
        seat= self.seat_list[time_choice]
        if seat[x][y]==0:
            cell=self.ws.cell(row=time_choice*len(seat) + (x+1),column= y+2)
            cell.value = 1
            self.wb.save(self.path)
            return 1
        else: return 0



if __name__ == '__main__':
    t=TheaterRepo()
    t.open_xlsx()
