import sqlite3


__all__ = ("ORM")




class ORM():
    """TODO"""
    
    def __init__(self, path):
        """
        TODO
        """
        
        self.connection = sqlite3.connect(path)
        
    def execute(self, q, params=()):
        """
        TODO
        """
        
        cursor = self.connection.cursor()
        data = [row for row in cursor.execute(q, params)]
        
        self.connection.commit()
        
        return data
