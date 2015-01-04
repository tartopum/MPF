from models.db import DBSelector
from models.serializer import Serializer
from views.line_drawer import LineDrawer
from workers.factory import Factory as WFactory

from analysis.linear_regression import linear_reg
from analysis.production import by_cons as prod_by_cons
from analysis.production import by_day as prod_by_day
from analysis.production import difference as prod_diff

from config import DATA_PATH



class Factory:
    
    def __init__(self):
        self.db = DBSelector()
        
        self.factory = WFactory(root=DATA_PATH, serializer=Serializer())
        
        self.line_drawer = LineDrawer
    
    def linear_reg(self, cow, force=False):
        linear_reg(cow, self.db, None, self.factory, force)
    
    def prod_by_cons(self, cow, force=False):
        prod_by_cons(cow, self.db, LineDrawer, self.factory, force)
        
    def prod_by_day(self, cow, force=False):
        prod_by_day(cow, self.db, LineDrawer, self.factory, force)
        
    def prod_diff(self, cow, force=False):
        prod_diff(cow, self.db, LineDrawer, self.factory, force)
