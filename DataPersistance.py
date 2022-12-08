#loading into/from files
import json
class Data:
    def load_from(self):
        with open('movies.json') as f:
            data = json.load(f)
        return data
    def load_into(self, data):
        with open('Movies_updated.json', 'w') as f:
            json.dump(data, f, indent=4)
        
        
data = Data()
info = data.load_from()
data.load_into(info)