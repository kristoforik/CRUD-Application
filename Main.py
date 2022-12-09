from ResourceManagement import management, check_title, check_number, creating_movie, find_movie
import time


class Application:
    def run(self):
        print("Main Menu")
        print("What do you want to do?")
        print("[1] Crate a movie")
        print("[2] Read a movie description")
        print("[3] Edit information about a movie")
        print("[4] Delete a movie from the list")
        attempt = input()
        if attempt == '1':
            movie = creating_movie()
            management.create(movie)     
        elif attempt == '2':
            id, title = find_movie()
            movie = management.read(id, title)
            if movie == False:
                print("No films found by these characteristics")
            else:
                id,title,year,genre = movie
                print(id, title, year, genre)
        elif attempt == '3':
            pass
        elif attempt == '4':
            pass
        else:
            time.sleep(0.5)
            print("Wrong input")
            time.sleep(1)
            self.run()


application = Application()
application.run()