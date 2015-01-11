class DataGroup:

    def __init__(self, name):
        self.name = name
        self.datasets = []
        
    def add(self, dataset):
        self.datasets.append(dataset)
