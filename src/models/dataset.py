class DataSet:

    def __init__(self, name, getters=[]):
        self.name = name
        self.contents = {}
        
        self.get(getters)
    
    def add(self, name, data):
        self.contents[name] = data
        
    def get(self, getters):
        for getter in getters:
            self.add(
                getter["name"], 
                getter["callable"](*getter["args"])
            )
