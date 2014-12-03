import sqlite3

class SQLQuery():
    def __init__(self, connection):
        self.connection = connection
        
    def execute(self, q, params=()):
        cursor = self.connection.cursor()
        data = [row for row in cursor.execute(q, params)]
        
        self.connection.commit()
        
        return data
