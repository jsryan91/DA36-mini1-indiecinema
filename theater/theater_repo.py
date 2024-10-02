from theater.theater_entity import *
import random
import datetime
from movie.movie_repo import *

class TheaterRepo:
    def __init__(self):

        self.date = datetime.datetime.now().strftime('%y%m%d') # excel-sheet를 date로 만들거임 !! >> 일단 해보자 ~** 안되면 말고

        #---MovieRepo에서 movie_list 가지고 오기-----------#
        self.movie_repo=MovieRepo()
        self.movie_list=self.movie_repo.get_movie_list()
        self.movie_name_list=[self.movie_list[i][0] for i in range(len(self.movie_list))]
        #--------------------------------------------------#

        #---TheaterEntity에서 상영시간(time_list), 좌석(seat_list) 가지고 오기---#
        self.theater_entity=Theater()
        self.time_list=self.theater_entity.get_time_list()
        self.seat_list = self.theater_entity.get_seat_list()
        # -----------------------------------------------------------------------#  구현완
        self.movie_time_list=[[time, random.choice(self.movie_name_list)] for time in self.time_list]
        self.answer=[]
        #-------------------------------------------------------------------------#
    def get_time_list(self, movie_choice): # 입력 받은 영화 번호의 상영시간을 가져오기 !!
        return self.movie_time_list[movie_choice]
#-------------------------------------------------------------------------#
    def get_seat_list(self,time_choice): #입력 받은 상영 시간에 >> 좌석 list를 가져오기
        return self.seat_list[time_choice]
#-------------------------------------------------------------------------#
    def possible_seat_choice(self, x, y,time_choice): # 고른자리가 구매가능한지 확인하기
        movie_seat=self.get_seat_list(time_choice)
        if movie_seat[x][y]==0:
            movie_seat[x][y]=1
            return 1
        else: return 0
#-------------------------------------------------------------------------#



















#=========================================================================#
# excel로 하려다가 실패함 >> 내일 다시 ,,
# self.open_xlsx()
#==========================================================================#
# #.xlsx
#     def open_xlsx(self):
#         path="C:/Workspaces/DA36-mini1-indiecinema/theater/theater.xlsx"
#         try:
#             self.wb = op.load_workbook(path)
#         except:
#             self.wb = op.Workbook()
#             self.wb.save(path)
#
#         print(self.wb)
#
#         for i in range(len(self.time_list)):
#             sheet=str(self.date)+"_"+str(self.time_list[i])
#             print(sheet)
#             if sheet not in self.wb.sheetnames:
#                 self.wb.create_sheet(title=sheet)
#                 self.wb.save(path)
#                 self.ws=self.wb[sheet]
#                 print(self.ws)
#                 self.temp_list = [[time, random.choice(self.movie_name_list)] for time in self.time_list]
#                 self.movie_time_list.append(self.temp_list)
#                 print(self.movie_time_list[i])
#                 cell=self.ws.cell(row=1,column=1)
#                 cell.value="/".join(map(str,self.temp_list[i]))
#                 print(self.seat_list)
#                 for i in range(len(self.seat_list)):
#                     for j in range(len(self.seat_list)):
#                         cell=self.ws.cell(row=i+1,column=j+2)
#                         cell.value=self.seat_list[i][j]
#             else:
#                 self.ws=self.wb[sheet]
#                 cell=self.ws.cell(row=1,column=1)
#                 self.movie_time_list.append(list(cell.value.split("/")))
#                 pass ## code 수정 필요
#
#         self.wb.save(path)
#
#
#     # def set_movie_time_list(self):
#
# #-------------------------------------------------------------------------#
#     def get_time_list(self, movie_choice): # 입력 받은 영화 번호의 상영시간을 가져오기 !!
#         return self.movie_time_list[movie_choice]
# #-------------------------------------------------------------------------#
#     def get_seat_list(self,time_choice): #입력 받은 상영 시간에 >> 좌석 list를 가져오기
#         num=self.time_list[time_choice]
#         sheet=str(self.date)+"_"+str(num)
#         self.ws=self.wb[sheet]
#         for i in range(len(self.seat_list)):
#             for j in range(len(self.seat_list)):
#                 cell= self.ws.cell(row=i+1, column=i + 1)
#                 self.seat_list[i][i]=cell.value
#
#         return self.seat_list[time_choice]
# #-------------------------------------------------------------------------#
#     def possible_seat_choice(self, x, y,time_choice): # 고른자리가 구매가능한지 확인하기
#         movie_seat=self.get_seat_list(time_choice)
#         if movie_seat[x][y]==0:
#             cell=self.ws.cell(row=x+1,column=y+1)
#             cell.value = 1
#             # cell.value=check된 좌석이라고 바꿔야함
#             return 1
#         else: return 0
# #-------------------------------------------------------------------------#


if __name__ == '__main__':
    repo=TheaterRepo()
    print(repo.get_time_list(1))
    print(repo.get_seat_list(2))
