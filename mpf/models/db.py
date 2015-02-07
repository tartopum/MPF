from mpf.models.sql import ORM



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
    
    def cow(self, cow):
        """
        TODO
        """
        
        q = "SELECT * FROM CrudeData WHERE cow = ?" 
        data = self.query(q, (int(cow),))
    
        d = {}
        
        for lact in self.lacts(cow):
            d[lact] = {
                "days": self.days(cow, lact),
                "prods": self.prods(cow, lact),
                "cons": self.cons(cow, lact)
            }
            
        return d
    
    def cons(self, cow, lact):
        """
        TODO
        """
        
        q = "SELECT cons FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY day" 
        data = self.query(q, (int(cow), lact))
        
        return [line[0] for line in data]
        
    def cows(self):
        """
        TODO
        """
        
        q = "SELECT DISTINCT cow FROM CrudeData"
        data = self.query(q)
        
        return [line[0] for line in data]
    
    def days(self, cow, lact):
        """
        TODO
        """
        
        q = "SELECT day FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY day" 
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
        
        q = "SELECT prod FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY day" 
        data = self.query(q, (int(cow), lact))
        
        return [line[0] for line in data]
       
