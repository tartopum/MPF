import drawers
from config import DATA_PATH

class BasicSaver:
    def __init__(self, folder):
        self.folder = folder
        self.data = []
        
    def add(self, data):
        self.data.append(data)
        
    def save(self):
        print(self.data)
