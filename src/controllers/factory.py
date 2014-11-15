from models.db import DBSelector
from views.line_drawer import LineDrawer
from workers.factory import Factory as WFactory

from controllers.linear_regression import linear_reg
from controllers.production import by_cons as prod_by_cons
from controllers.production import by_day as prod_by_day
from controllers.production import difference as prod_diff



class Factory:
    
    def __init__(self):
        self.factory = WFactory()
        
        self.db = DBSelector()
        
        self.line_drawer = LineDrawer
    
    def linear_reg(self, cow, force=False):
        linear_reg(cow, self.db, None, self.factory, force)
    
    def prod_by_cons(self, cow, force=False):
        prod_by_cons(cow, self.db, LineDrawer, self.factory, force)
        
    def prod_by_day(self, cow, force=False):
        prod_by_day(cow, self.db, LineDrawer, self.factory, force)
        
    def prod_diff(self, cow, force=False):
        prod_diff(cow, self.db, LineDrawer, self.factory, force)
