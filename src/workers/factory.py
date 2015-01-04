from os.path import join

from workers.workers import Difference 
from workers.workers import Identity
from workers.workers import LinearRegression
from workers.workers import MovingAveraging
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
        obj = Difference()
        
        return self.get_worker(obj, dest, force)

    def Identity(self, dest, force=False):
        obj = Identity()
        
        return self.get_worker(obj, dest, force)

    def LinearRegression(self, percentage, dest, force=False):
        obj = LinearRegression(percentage)
        
        return self.get_worker(obj, dest, force)

    def MovingAveraging(self, step, dest, force=False):
        obj = MovingAveraging(step)
        
        return self.get_worker(obj, dest, force)
        
    def WorkingGroup(self, cow, drawer=None):
        return WorkingGroup(cow, drawer)
        
        
