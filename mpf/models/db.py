from mpf.models.sql import ORM
from mpf.models.data import Cow, Data, Lact



__all__ = ["DBSelector"]



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
        q = "SELECT * FROM CrudeData WHERE cow = ?" 
        data = self.query(q, (int(cow_num),))
    
        cow = Cow(cow_num)
        
        for lact_num in self.lacts(cow_num):
            cow.add_lact(lact_num, self.lact(cow_num, lact_num))
            
        return cow
        
    def cows(self):
        """
        TODO
        """
        
        q = "SELECT DISTINCT cow FROM CrudeData"
        data = self.query(q)
        
        return [line[0] for line in data]
    
    def data(self):
        data = Data()
        
        for num in self.cows():
            data.add_cow(num, self.cow(num))
        
        return data
    
    def days(self, cow, lact):
        """
        TODO
        """
        
        q = "SELECT day FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY day" 
        data = self.query(q, (int(cow), lact))
        
        return [line[0] for line in data]
    
    def lact(self, cow_num, lact_num):
        return Lact(lact_num, self.days(cow_num, lact_num), 
                    self.prods(cow_num, lact_num), self.cons(cow_num, lact_num))
        
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
       
