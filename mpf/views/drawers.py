import matplotlib.pyplot as plt



__all__ = ("LineDrawer")



class Drawer:
    """TODO"""
    
    X_INDEX = 0
    Y_INDEX = 1

    def __init__(self, xlabel="x", ylabel="y"):
        """TODO"""
        
        self.xlabel = xlabel
        self.ylabel = ylabel
        
        self.clear()
        
    def add(self, x, y):
        """TODO"""
            
        self.data.append((x, y))
    
    def clear(self):
        """TODO"""
        
        plt.close()
        
        self.data = []
        
    def draw(self):
        raise RuntimeError("'draw' method must be implemented.")
    
    def save(self, dest):
        """TODO"""
        
        plt.clf()
        
        self.draw()
        plt.savefig(dest, dpi=250)
        print(dest + " saved.")
        
        self.clear()
        
    def show(self):
        """TODO"""
        
        plt.clf()
        
        self.draw()
        plt.show()
        
        self.clear() 
    
    
class LineDrawer(Drawer):
    """TODO"""

    def __init__(self, xlabel="x", ylabel="y", plot_style=""):
        """TODO"""
        
        Drawer.__init__(self, title, xlabel, ylabel)
        
        self.plot_style = plot_style
        
    def draw(self):
        """TODO"""
        
        l = len(self.data)
        
        fig = plt.figure(figsize=(4, 2.5*(l+1)))
        
        plt.subplot(l+1, 1, 1)
        
        for k in range(l):
            x = self.data[k][Drawer.X_INDEX]
            y = self.data[k][Drawer.Y_INDEX]
            
            plt.subplot(l+1, 1, k+2) 
            plt.plot(x, y, self.plot_style)
            plt.grid(True)
            plt.xlabel(self.xlabel)
            plt.ylabel(self.ylabel)
        
        fig.tight_layout() # To space subplots
