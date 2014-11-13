from sql import SQLManager

class Selector:
    def __init__(self, connection):
        self.sql_manager = SQLManager(connection)
        
    def query(self, q, params=()):
        return self.sql_manager.execute(q, params)
    
    def get_cons(self, cow, lact):
        q = "SELECT cons FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY lact_day" 
        data = self.query(q, (cow, lact))
        
        return [line[0] for line in data]
        
    def get_cows(self):
        q = "SELECT DISTINCT cow FROM CrudeData"
        data = self.query(q)
        
        return [line[0] for line in data]
    
    def get_lact_days(self, cow, lact):
        q = "SELECT lact_day FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY lact_day" 
        data = self.query(q, (cow, lact))
        
        return [line[0] for line in data]
        
    def get_lacts(self, cow):
        # We only work on the whole lactation
        q = "SELECT DISTINCT lact FROM CrudeData WHERE cow = ?"
        data = self.query(q, (cow,))
        
        return [line[0] for line in data]
        
    def get_prods(self, cow, lact):
        q = "SELECT prod FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY lact_day" 
        data = self.query(q, (cow, lact))
        
        return [line[0] for line in data]
