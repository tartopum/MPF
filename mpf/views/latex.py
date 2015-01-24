import numpy as np

from pylatex import Document, Section, Math
from pylatex.numpy import Matrix, VectorName



class LaTeX:

    def __init__(self, title):
        self.data = []
        
        self.doc = Document(title=title)
    
    def add(self, name, data):
        self.data.append((name, data))
    
    def parse(self, k, v):
        if type(v).__module__ == np.__name__:
            return str(k), Matrix(v)
        else:
            return str(k), str(v)
    
    def draw(self):
        for name, data in self.data:
            with self.doc.create(Section(name)):
                for k, v in data.items():
                    k, v = self.parse(k, v)
                    
                    self.doc.append(Math(data=[k, "=", v]))
    
    def save(self, dest):
        self.doc.filename = dest
        
        self.draw()
        
        self.doc.generate_tex()
            
        
if __name__ == "__main__":
    latex = LaTeX("0001")
    
    A = np.vstack([
        [1,2],
        [3,4],
        [5,6]
    ])
    
    data = {
        "A": A,
        "error": 12.45684316489
    }
    
    latex.add("lactation 1", data)
    
    latex.save("./test")
