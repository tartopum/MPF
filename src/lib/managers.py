from os.path import join
from copy import deepcopy

import lib.processors as processors
from lib.selectors import FileSelector

from config import DATA_PATH

class Factory:
    def __init__(self):
        self.root = DATA_PATH

    def Difference(self, dest):
        return Difference(join(self.root, dest))

    def MovingAverage(self, step, dest):
        return MovingAverage(step, join(self.root, dest))
        
    def WorkingGroup(self, cow, dest, drawer):
        return WorkingGroup(cow, join(self.root, dest), drawer)

class Manager:
    def __init__(self, dest):
        self.data = None
        self.dest = dest
        
        self.file_selector = FileSelector()
        
    def __rshift__(self, next):
        next.data = deepcopy(self.data)
        next.work()
        
    def work(self):
        data = self.file_selector.load(self.dest)
        
        if data is not None:
            self.data = data
        else:
            for series in self.data.series:
                series.x, series.y = self.processor.work(series.x, series.y)
                
                self.data.drawer.add(series.x, series.y, series.name)
            
            self.data.drawer.save(self.dest)
            self.file_selector.save(self.data, self.dest)

class Difference(Manager):
    def __init__(self, dest):
        Manager.__init__(self, dest)
        
        self.processor = processors.Difference()

class LinearRegression(Manager):
    def __init__(self, dest):
        Manager.__init__(self, dest)
        
        self.processor = processors.LinearRegression()
        
    def work(self):
        pass

class MovingAverage(Manager):
    def __init__(self, step, dest):
        Manager.__init__(self, dest)
        
        self.step = max(1, int(step)) # 'step' is an integer greater than 1
        
        self.processor = processors.MovingAverage(self.step)

class Series:
    def __init__(self):
        self.name = []
        self.x = []
        self.y = []
        
class WorkingGroup(Manager):
    def __init__(self, cow, dest, drawer):
        Manager.__init__(self, dest)
        
        self.cow = cow
        self.series = []
        
        self.data = self # To make __rshift__ work
        self.drawer = drawer
        self.processor = processors.Identity()
        
    def fill(self, name_getter, x_getter, y_getter):
        names = name_getter["fn"](self.cow)
        
        for name in names:
            series = Series()
            series.name = name_getter["prefix"] + str(name) + name_getter["suffix"]
            series.x = x_getter(self.cow, name)
            series.y = y_getter(self.cow, name)
            
            self.series.append(series)        
    
