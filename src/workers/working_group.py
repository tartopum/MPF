class Series:

    def __init__(self):
        self.id = -1
        self.name = ""
        self.data = {}

        
class WorkingGroup:

    def __init__(self, cow, view):
        self.cow = cow
        self.series = []
        
        self.view = view
        
    def fill(self, namer, getters):
        names = namer["getter"](self.cow)
        
        for name in names:
            series = Series()
            series.id = name
            series.name = namer["prefix"] + str(name) + namer["suffix"]
            
            for key, getter in getters.items():
                series.data[key] = getter(self.cow, name)
            
            self.series.append(series)
            
    def clear_series(self):
        self.series = []
