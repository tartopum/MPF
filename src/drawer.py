from math import sqrt, ceil
import matplotlib.pyplot as plt

class Drawer:
    def __init__(self, title=""):
        self.title = title
        self.clear()
        
        self.X_INDEX = 0
        self.Y_INDEX = 1
        self.TITLE_INDEX = 2
        self.XLABEL_INDEX = 3
        self.YLABEL_INDEX = 4
        
    def add(self, x, y, title="", xlabel="x", ylabel="y"):
        self.data.append((x, y, title, xlabel, ylabel))
    
    def clear(self):
        plt.clf()
        self.data = []
        
    def draw(self):
        l = len(self.data)
        cols = int(ceil(sqrt(l)))
        lines = int(ceil(l/cols))
        
        fig = plt.figure(num=1, figsize=(10, 8))
        fig.suptitle(self.title)
        
        for k in range(l):
            x = self.data[k][self.X_INDEX]
            y = self.data[k][self.Y_INDEX]
            title = self.data[k][self.TITLE_INDEX]
            xlabel = self.data[k][self.XLABEL_INDEX]
            ylabel = self.data[k][self.YLABEL_INDEX]
             
            plt.subplot(lines, cols, k+1)
            plt.plot(x, y)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.grid(True)
            plt.title(title)
        
        plt.tight_layout() # To space subplots
        plt.subplots_adjust(top=0.9) # Not to overwrite title
    
    def save(self, dest):
        self.draw()
        plt.savefig(dest)
        self.clear()
        
    def show(self):
        self.draw()
        plt.show()
        self.clear()


if __name__ == "__main__":
    drawer = Drawer("TITLE")
    
    n = 6
    for i in range(n):
        drawer.add(list(range(i+2)), list(range(i+2)), str(i), "x" + str(i), "y" + str(i))
    drawer.show()
    
    
