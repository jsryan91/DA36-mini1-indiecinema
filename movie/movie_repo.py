import datetime, os

class MovieRepo:
    def __init__(self):
        self.movie_list=[]
        self.date = datetime.datetime.now().strftime('%y%m%d')
        self.set_movie_list()
#-------------------------------------------------------------------------#
    def set_movie_list(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        movie_file_path = os.path.join(current_dir, 'movie.txt')
        with open(movie_file_path, 'r', encoding='utf-8') as f:
            text_line = f.read()
            text_line=text_line.split("\n")
            for i in range(len(text_line)):
                text_line[i]=list(text_line[i].split(","))
                if int(text_line[i][1])>=int(self.date):
                    self.movie_list.append(text_line[i])
#-------------------------------------------------------------------------#
    def get_movie_list(self):
        return self.movie_list

    def get_title(self, movie_index):
        return self.movie_list[movie_index][0]