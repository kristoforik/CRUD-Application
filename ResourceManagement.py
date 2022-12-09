#create, read, update, delete
from DataPersistance import data

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



class Management:
    def create(self):   
        info = data.load_from()
        movie = creating_movie()
        info["movies"].append(movie)
        #print(info)
        data.load_into(info)
    def read(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass

management = Management()
management.create()




