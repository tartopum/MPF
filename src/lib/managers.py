from os.path import join

import lib.processors as processors
from lib.models import FileManager

from config import DATA_PATH

class Factory:
    def __init__(self):
        self.root = DATA_PATH

    def Difference(self, dest, force=False):
        return Difference(join(self.root, dest), force)

    def Identity(self, dest, force=False):
        return Identity(join(self.root, dest), force)

    def LinearRegression(self, percentage, dest, force=False):
        return LinearRegression(percentage, join(self.root, dest), force)

    def MovingAverage(self, step, dest, force=False):
        return MovingAverage(step, join(self.root, dest), force)
        
    def WorkingGroup(self, cow, drawer=None):
        return WorkingGroup(cow, drawer)

#
# Abstract managers
#
class Manager:
    def __init__(self, dest, force):
        self.data = None
        self.dest = dest
        self.force = force
        
        self.file_manager = FileManager()
        
    def work(self):
        raise RuntimeError("'work' method must be implemented.")
        
class XYManager(Manager):
    def __init__(self, dest, force):
        Manager.__init__(self, dest, force)
        
    def work(self, wg):
        if not self.force: 
            cache = self.file_manager.load(self.dest)
            
            if cache is not None:
                return cache
        
        # Build data
        for series in wg.series:
            x = series.data["x"]
            y = series.data["y"]
            
            x, y = self.processor.work(x, y)
            
            wg.drawer.add(x, y, series.name)
        
        wg.drawer.save(self.dest)
        self.file_manager.save(wg, self.dest)
        
        return wg

#
# Managers
#
class Difference(XYManager):
    def __init__(self, dest, force):
        XYManager.__init__(self, dest, force)
        
        self.processor = processors.Difference()

class Identity(XYManager):
    def __init__(self, dest, force):
        XYManager.__init__(self, dest, force)
        
        self.processor = processors.Identity()

class LinearRegression(Manager):
    def __init__(self, percentage, dest, force):
        Manager.__init__(self, dest, force)
        
        self.alea = processors.AleaValues(percentage)
        self.processor = processors.LinearRegression()
    
    def build_A(self, data):
        A = []
        l = len(data[0])
        
        for i in range(l):
            line = [1] # Offset
            
            for series in data:
                line.append(series[i])
                line.append(series[i]**2)
            
            A.append(line)
            
        return A
        
    def work(self, wg):
        if not self.force: 
            cache = self.file_manager.load(self.dest)
            
            if cache is not None:
                return cache
        
        # Build data
        for series in wg.series:
            cons = series.data["cons"]
            lact_days = series.data["lact_days"]
            lact = [series.id for i in range(len(cons))]
            
            B = series.data["prods"]
            A = self.build_A([cons, lact_days, lact])
            
            A_alea, B_alea = self.alea.work([A, B])
            
            series.data["A"] = A
            series.data["B_alea"] = B_alea
            series.data["A_alea"] = A_alea
            
            X = self.processor.work(A_alea, B_alea)
            series.data["X"] = X
            
            diff = self.processor.compare(A, X, B)
            series.data["diff"] = diff
            
            print(diff)
            
        # self.file_manager.save(wg, self.dest)
        
        return wg

class MovingAverage(XYManager):
    def __init__(self, step, dest, force):
        XYManager.__init__(self, dest, force)
        
        self.step = max(1, int(step)) # 'step' is an integer greater than 1
        
        self.processor = processors.MovingAverage(self.step)

#
# Working group
#
class Series:
    def __init__(self):
        self.id = -1
        self.name = ""
        self.data = {}
        
class WorkingGroup:
    def __init__(self, cow, drawer):
        self.cow = cow
        self.series = []
        
        self.drawer = drawer
        
    def fill(self, namer, getters):
        names = namer["getter"](self.cow)
        
        for name in names:
            series = Series()
            series.id = name
            series.name = namer["prefix"] + str(name) + namer["suffix"]
            
            for key, getter in getters.items():
                series.data[key] = getter(self.cow, name)
            
            self.series.append(series)        
    
