from config import DATA_PATH

class Manager:
    def __init__(self):
        pass
        
    def work(self, dest, processor, data):
        return processor.process(*data)
