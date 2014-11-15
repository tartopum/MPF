import pickle

class Serializer:
    def __init__(self):
        pass
    
    def load(self, src):
        src += ".data"
        
        try:    
            f = open(src, "rb")
            contents = pickle.load(f)
        except:
            contents = None
        else:
            f.close()
            
        return contents
        
    def save(self, data, dest):
        dest += ".data"
        
        with open(dest, "wb") as f:
            pickle.dump(data, f)
            
        print(dest + " saved.")
