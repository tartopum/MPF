from utils.sql import ORM
from config import DATABASE_PATH

class DBSelector:
    def __init__(self):
        self.orm = ORM(DATABASE_PATH)
        
    def query(self, q, params=()):
        return self.orm.execute(q, params)
    
    def cons(self, cow, lact):
        q = "SELECT cons FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY lact_day" 
        data = self.query(q, (cow, lact))
        
        return [line[0] for line in data]
        
    def cows(self):
        q = "SELECT DISTINCT cow FROM CrudeData"
        data = self.query(q)
        
        return [line[0] for line in data]
    
    def lact_days(self, cow, lact):
        q = "SELECT lact_day FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY lact_day" 
        data = self.query(q, (cow, lact))
        
        return [line[0] for line in data]
        
    def lacts(self, cow):
        q = "SELECT DISTINCT lact FROM CrudeData WHERE cow = ?"
        data = self.query(q, (cow,))
        
        return [line[0] for line in data]
        
    def prods(self, cow, lact):
        q = "SELECT prod FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY lact_day" 
        data = self.query(q, (cow, lact))
        
        return [line[0] for line in data]
       
