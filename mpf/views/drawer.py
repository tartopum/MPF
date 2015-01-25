import matplotlib.pyplot as plt

from mpf.views.abstracts import View



__all__ = ["Drawer"]



class Drawer(View):
    """TODO"""

    def __init__(self, title="", xlabel="x", ylabel="y"):
        """
        TODO
        """
        
        self.ext = ".png"
        
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        
        self.clear()
        
        self.X_INDEX = 0
        self.Y_INDEX = 1
        self.TITLE_INDEX = 2
        
    def add(self, data):
        """
        TODO
        """
        
        x = data["x"]
        y = data["y"]
        
        try:
            title = data["title"]
        except KeyError:
            title = ""
            
        self.data.append((x, y, title))
    
    def clear(self):
        """
        TODO
        """
        
        plt.close()
        
        self.data = []
        
    def draw(self):
        raise RuntimeError("'draw' method must be implemented.")
    
    def save(self, dest):
        """
        TODO
        """
        
        dest = self._add_ext(dest)
        
        plt.clf()
        
        self.draw()
        plt.savefig(dest, dpi=250)
        print(dest + " saved.")
        
        self.clear()
        
    def show(self):
        """
        TODO
        """
        
        plt.clf()
        
        self.draw()
        plt.show()
        
        self.clear() 
    
