import json



class JSONWriter:
    
    def __init__(self):
        self.data = {}
        
    def add(self, d):
        self.data.update(d)
        
    def show(self):
        print(self.data)
        
    def save(self, dest):
        dest += ".json"
        
        with open(dest, "w") as f:
            json.dump(self.data, f, indent = 4)
            
        print(dest + " saved.")
