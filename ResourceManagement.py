#create, read, update, delete
from DataPersistance import data
info = data.load_from()

#ID, title, year, genre
def creating_movie():
    id = input("Enter an ID for a film: ")
    id = check_number(id)
    title = input("Enter a title for your film: ")
    title = check_title(title)
    year = input("Enter a year of your film: ")
    year = check_number(year)
    genre = input("Enter a genre of your film: ")
    genre = check_genre(genre)
    return {'ID': id, 'title': title, 'year': year, 'genre': genre}

def updating_movie():
    title = input("Enter a new title for your film: ")
    #title = check_title(title)
    year = input("Enter a new year of your film: ")
    year = check_number(year)
    genre = input("Enter a new genre of your film: ")
    genre = check_genre(genre)
    return title, year, genre

def find_movie():
    id = input("Enter an ID of the film: ")
    id = check_number(id)
    title = input("Enter a title of the film: ")
    #title = check_title(title)
    return id, title

def updating_list(old_movie, new_movie):
    title, year, genre, = new_movie
    for movie in info['movies']:
        if movie['title'] == old_movie['title'] and movie['year'] == old_movie['year'] and movie['genre'] == old_movie['genre']:
            movie['title'] = title
            movie['year'] = year
            movie['genre'] = genre
            #print(movie)
    return info
        
def check_number(num):
    while True:
        try:
            int(num)
            return num
        except:
            num = input("Enter a valid number: ")
        
def check_title(title):
    while title.isalpha() != True:
        title = input("Enter a valid title: ")
    return title

def check_genre(title):
    while title.isalpha() != True:
        title = input("Enter a valid genre: ")
    return title

def check_if_exists(id, title):
    for movie in info['movies']:
        if movie['ID'] == id and movie['title'] == title:
            return movie

def check_by_id(id):
    for movie in info['movies']:
        if movie['ID'] == id:
            return movie




class Management:
    def create(self, movie):   
        info["movies"].append(movie)
        data.load_into(info)
    def read(self, id, title):
        movie = check_if_exists(id, title)
        if movie == None:
            return False
        else: 
            title = movie['title']
            year = movie['year']
            genre = movie['genre']
            return id, title, year, genre
    def update(self, movie, new_movie):
        new_list = updating_list(movie, new_movie)
        data.load_into(new_list)
    def delete(self, movie):
        info['movies'].remove(movie)
        data.load_into(info)

management = Management()
