from ResourceManagement import management, check_title, check_number, creating_movie, find_movie, check_by_id, updating_movie
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
                time.sleep(0.5)
                print("No films found by these characteristics")
                time.sleep(1)
                self.run()
            else:
                id,title,year,genre = movie
                print(id, title, year, genre)
        elif attempt == '3':
            id = input('Enter an ID to find a film: ')
            id = check_number(id)
            movie = check_by_id(id)
            if movie == None:
                time.sleep(0.5)
                print("There is no film with such ID")
                time.sleep(1)
                self.run()
            else:
                title, year, genre = updating_movie()
                new_movie = title, year, genre
                management.update(movie, new_movie)
        elif attempt == '4':
            id = input('Enter an ID to find a film: ')
            id = check_number(id)
            movie = check_by_id(id)
            if movie == None:
                time.sleep(0.5)
                print("ID is invalid")
                time.sleep(1)
                self.run()
            else:
                management.delete(movie)
        else:
            time.sleep(0.5)
            print("Wrong input")
            time.sleep(1)
            self.run()


application = Application()
application.run()