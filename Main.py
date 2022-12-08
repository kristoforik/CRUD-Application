import ResourceManagement, DataPersistance
class Application:
    management = ResourceManagement()
    data = DataPersistance()
    def run():
        print("What do you want to do?")
        print("[1] Crate a movie")
        print("[2] Read a movie description")
        print("[3] Edit information about a movie")
        print("[4] Delete a movie from the list")
        attempt = input()
        if attempt == 1:
            pass