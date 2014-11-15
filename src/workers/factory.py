from os.path import join

from config import DATA_PATH

from workers.workers import Difference, Identity, LinearRegression, MovingAveraging
from workers.working_group import WorkingGroup



class Factory:

    def __init__(self):
        self.root = DATA_PATH

    def Difference(self, dest, force=False):
        return Difference(join(self.root, dest), force)

    def Identity(self, dest, force=False):
        return Identity(join(self.root, dest), force)

    def LinearRegression(self, percentage, dest, force=False):
        return LinearRegression(percentage, join(self.root, dest), force)

    def MovingAveraging(self, step, dest, force=False):
        return MovingAveraging(step, join(self.root, dest), force)
        
    def WorkingGroup(self, cow, drawer=None):
        return WorkingGroup(cow, drawer)
