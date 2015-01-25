import numpy as np

from pylatex import Document, Section, Math
from pylatex.numpy import Matrix, VectorName


__all__ = ["LaTeX"]



class LaTeX:
    """TODO"""

    def __init__(self, title):
        """
        TODO
        """
        
        self.data = []
        
        self.doc = Document(title=title)
    
    def add(self, name, data):
        """
        TODO
        """
        
        self.data.append((name, data))
    
    def parse(self, k, v):
        """
        TODO
        """
        
        if type(v).__module__ == np.__name__:
            return str(k), Matrix(v)
        else:
            return str(k), str(v)
    
    def draw(self):
        """
        TODO
        """
        
        for name, data in self.data:
            with self.doc.create(Section(name)):
                for k, v in data.items():
                    k, v = self.parse(k, v)
                    
                    self.doc.append(Math(data=[k, "=", v]))
    
    def save(self, dest):
        """
        TODO
        """
        
        self.doc.filename = dest
        
        self.draw()
        
        self.doc.generate_tex()
