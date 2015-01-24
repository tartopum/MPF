from models.db import DBSelector
from models.serializer import Serializer
from views.line_drawer import LineDrawer
from views.json import JSONWriter
from workers.factory import Factory as WFactory

from analysis import linear_regression as lr
from analysis import production as prod

from config import DATA_PATH



class Factory:
    
    def __init__(self):
        self.db = DBSelector()
        
        self.factory = WFactory(root=DATA_PATH, serializer=Serializer())
    
    def linear_reg(self, cow, force=False):
        lr.linear_reg(cow, self.db, JSONWriter, self.factory, force)
        
    def linear_reg_stats(self, cow, force=False):
        lr.linear_reg_stats(cow, self.db, JSONWriter, self.factory, force)
    
    def prod_by_cons(self, cow, force=False):
        prod.by_cons(cow, self.db, LineDrawer, self.factory, force)
        
    def prod_by_day(self, cow, force=False):
        prod.by_day(cow, self.db, LineDrawer, self.factory, force)
        
    def prod_diff(self, cow, force=False):
        prod.difference(cow, self.db, LineDrawer, self.factory, force)
