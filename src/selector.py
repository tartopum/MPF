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
        
    def get_lactations(self, cow):
        q = "SELECT DISTINCT lac FROM CrudeData WHERE cow = ?"
        data = self.query(q, (cow,))
        
        return [line[0] for line in data]
