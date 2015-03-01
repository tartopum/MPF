from mpf.models.sql import ORM
from mpf.models.data import DataDict


__all__ = ("DBSelector")



class DBSelector:
    """TODO"""
    
    def __init__(self, db_path):
        self.orm = ORM(db_path)
        
    def query(self, q, params=()):
        """
        TODO
        """
        
        return self.orm.execute(q, params)
    
    def cons(self, cow, lact):
        """
        TODO
        """
        
        q = "SELECT cons FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY day" 
        data = self.query(q, (int(cow), lact))
        
        return [line[0] for line in data]
    
    def cow(self, cow_num):
        cow = DataDict()
        
        for lact_num in self.lacts(cow_num):
            key = (DataDict.lact_label, lact_num)
            cow[key] = self.lact(cow_num, lact_num)
            
        return cow
        
    def cows(self):
        """
        TODO
        """
        
        q = "SELECT DISTINCT cow FROM CrudeData"
        data = self.query(q)
        
        return [line[0] for line in data]
    
    def data(self):
        data = DataDict()
        
        for num in self.cows():
            key = (DataDict.cow_label, num)
            data[key] = self.cow(num)
        
        return data
    
    def days(self, cow, lact):
        """
        TODO
        """
        
        q = "SELECT day FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY day" 
        data = self.query(q, (int(cow), lact))
        
        return [line[0] for line in data]
    
    def lact(self, cow_num, lact_num):
        cow_key = key = (DataDict.cow_label, cow_num)
        lact = DataDict(cow_key)
        
        lact["cons"] = self.cons(cow_num, lact_num)
        lact["days"] = self.days(cow_num, lact_num)
        lact["prods"] = self.prods(cow_num, lact_num)
            
        return lact
        
    def lacts(self, cow):
        """
        TODO
        """
        
        q = "SELECT DISTINCT lact FROM CrudeData WHERE cow = ?"
        data = self.query(q, (int(cow),))
        
        return [line[0] for line in data]
        
    def prods(self, cow, lact):
        """
        TODO
        """
        
        q = "SELECT prod FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY day" 
        data = self.query(q, (int(cow), lact))
        
        return [line[0] for line in data]
       
