import sqlite3

class ORM():
    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        
    def execute(self, q, params=()):
        cursor = self.connection.cursor()
        data = [row for row in cursor.execute(q, params)]
        
        self.connection.commit()
        
        return data
