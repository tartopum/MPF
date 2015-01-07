from os.path import join

from workers import workers
from workers.working_group import WorkingGroup



class Factory:

    def __init__(self, root, serializer):
        self.root = root
        self.serializer = serializer

    def get_worker(self, obj, dest, force):
        obj.dest = join(self.root, dest)
        obj.force = force
        obj.serializer = self.serializer
        
        return obj

    def Difference(self, dest, force=False):
        obj = workers.Difference()
        
        return self.get_worker(obj, dest, force)

    def Identity(self, dest, force=False):
        obj = workers.Identity()
        
        return self.get_worker(obj, dest, force)

    def LinearRegression(self, percentage, dest, force=False):
        obj = workers.LinearRegression(percentage)
        
        return self.get_worker(obj, dest, force)

    def MovingAveraging(self, step, dest, force=False):
        obj = workers.MovingAveraging(step)
        
        return self.get_worker(obj, dest, force)
    
    def Statistics(self, dest, key, force=False):
        obj = workers.Statistics(key)
        
        return self.get_worker(obj, dest, force)
        
    def WorkingGroup(self, cow, drawer=None):
        return WorkingGroup(cow, drawer)
        
        
