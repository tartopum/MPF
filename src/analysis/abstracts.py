from models.dataset import DataSet
from models.datagroup import DataGroup
from models.serializer import Serializer

from workers.factory import Factory

from config import DATA_PATH



class Analysis:
    """
        TODO
    """
    
    def __init__(self, name):
        self.datagroup = DataGroup(name)
        
        self.factory = Factory(DATA_PATH, Serializer())

        
class XYAnalysis(Analysis):
    """
        TODO
    """
    
    def __init__(self, name, xgetter, ygetter):
        Analysis.__init__(self, name)
        
        self.xgetter = xgetter
        self.ygetter = ygetter
    
    def add(self, name, *args):
        args = (self.datagroup.name,) + args
        
        self.datagroup.add(DataSet(
            name,
            [
                {
                    "name": "x",
                    "callable": self.xgetter,
                    "args": args
                },
                {    
                    "name": "y",
                    "callable": self.ygetter,
                    "args": args
                }
            ]
        ))
        

class LinRegAnalysis(Analysis):
    """
        TODO
    """
    
    def __init__(self, name):
        Analysis.__init__(self, name)

    def add(self, name, *args):
        args = (self.datagroup.name,) + args
        
        self.datagroup.add(DataSet(
            name,
            [
                {
                    "name": "B",
                    "callable": self.B_callable,
                    "args": args
                },
                {
                    "name": "A-data",
                    "callable": self.get_A,
                    "args": args
                }
            ]
        ))
