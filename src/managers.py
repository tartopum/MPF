from os.path import join
from copy import deepcopy

import processors
from saver import Saver

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
        
        self.saver = Saver(self.dest)
        
    def __rshift__(self, next):
        data = deepcopy(self.data)
        next.work(data)
        
    def work(self):
        raise RuntimeError("'work' method must be implemented.")

class WorkingGroup(Manager):
    class Series:
        def __init__(self):
            self.name = []
            self.x = []
            self.y = []
            
    def __init__(self, cow, dest, drawer):
        Manager.__init__(self, dest)
        
        self.cow = cow
        self.series = []
        
        self.data = self # To make __rshift__ work
        self.drawer = drawer
        
    def fill(self, name_getter, x_getter, y_getter):
        names = name_getter(self.cow)
        
        for name in names:
            series = WorkingGroup.Series()
            series.name = name
            series.x = x_getter(self.cow, name)
            series.y = y_getter(self.cow, name)
            
            self.series.append(series)
            
    def work(self):
        for series in self.series:
            self.drawer.add(series.x, series.y, series.name)
        
        self.drawer.show()

class Difference(Manager):
    def __init__(self, dest):
        Manager.__init__(self, dest)
        
        self.processor = processors.Difference()
        
    def work(self, data):
        self.data = data
        
        for series in self.data.series:
            series.x, series.y = self.processor.work(series.x, series.y)
            
            self.data.drawer.add(series.x, series.y, series.name)
            
        self.data.drawer.show()
        self.saver.save(self.data)

class MovingAverage(Manager):
    def __init__(self, step, dest):
        Manager.__init__(self, dest)
        
        self.step = max(1, int(step)) # 'step' is an integer greater than 1
        
        self.processor = processors.MovingAverage(self.step)
        
    def work(self, data):
        self.data = data
        
        # Cache
        # TODO
        
        for series in self.data.series:
            series.x, series.y = self.processor.work(series.x, series.y)
            
            self.data.drawer.add(series.x, series.y, series.name)
        
        self.data.drawer.show()
        self.saver.save(self.data)
        
