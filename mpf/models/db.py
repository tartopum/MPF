import sqlite3

from mpf.tools import CONS_LBL, COW_LBL, CRUDE_LBL, DAYS_LBL, LACT_LBL, PRODS_LBL

__all__ = ("DBSelector")



class DBSelector:
    """TODO"""
    
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        
    def query(self, q, params=()):
        """TODO"""
        
        cursor = self.connection.cursor()
        data = [row for row in cursor.execute(q, params)]
        
        self.connection.commit()
        
        return data
    
    def cons(self, cow, lact):
        """TODO"""
        
        q = "SELECT cons FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY day" 
        data = self.query(q, (cow, lact))
        
        return [line[0] for line in data]
        
    def cows(self):
        """TODO"""
        
        q = "SELECT DISTINCT cow FROM CrudeData"
        data = self.query(q)
        
        return [line[0] for line in data]
    
    def data(self):
        """TODO"""
        
        data = DataDict(None, None)
        
        for cow_num in self.cows():
            cow_key = (COW_LBL, cow_num)
            cow = data.add_child(cow_key)
            
            for lact_num in self.lacts(cow_num):
                lact_key = (LACT_LBL, lact_num)
                lact = cow.add_child(lact_key)
                
                lact[(CRUDE_LBL, CONS_LBL)] = self.cons(cow_num, lact_num)
                lact[(CRUDE_LBL, DAYS_LBL)] = self.days(cow_num, lact_num)
                lact[(CRUDE_LBL, PRODS_LBL)] = self.prods(cow_num, lact_num)
        
        return data
    
    def days(self, cow, lact):
        """TODO"""
        
        q = "SELECT day FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY day" 
        data = self.query(q, (cow, lact))
        
        return [line[0] for line in data]
        
    def lacts(self, cow):
        """TODO"""
        
        q = "SELECT DISTINCT lact FROM CrudeData WHERE cow = ?"
        data = self.query(q, (int(cow),))
        
        return [line[0] for line in data]
        
    def prods(self, cow, lact):
        """TODO"""
        
        q = "SELECT prod FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY day" 
        data = self.query(q, (cow, lact))
        
        return [line[0] for line in data]
       
