from .sql import ORM



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
        
        q = "SELECT cons FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY lact_day" 
        data = self.query(q, (int(cow), lact))
        
        return [line[0] for line in data]
        
    def cows(self):
        """
        TODO
        """
        
        q = "SELECT DISTINCT cow FROM CrudeData"
        data = self.query(q)
        
        return [line[0] for line in data]
    
    def lact_days(self, cow, lact):
        """
        TODO
        """
        
        q = "SELECT lact_day FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY lact_day" 
        data = self.query(q, (int(cow), lact))
        
        return [line[0] for line in data]
        
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
        
        q = "SELECT prod FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY lact_day" 
        data = self.query(q, (int(cow), lact))
        
        return [line[0] for line in data]
       
