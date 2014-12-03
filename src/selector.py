class Selector:
    def __init__(self, connection):
        self.connection = connection
        
    def query(self, q, params=()):
        cursor = self.connection.cursor()
        data = [row for row in cursor.execute(q, params)]
        
        self.connection.commit()
        
        return data
        
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
        q = "SELECT DISTINCT lact FROM CrudeData WHERE cow = ? AND lact_day = 1"
        data = self.query(q, (cow,))
        
        return [line[0] for line in data]
        
    def get_prods(self, cow, lact):
        q = "SELECT prod FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY lact_day" 
        data = self.query(q, (cow, lact))
        
        return [line[0] for line in data]
