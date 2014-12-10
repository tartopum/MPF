from math import sqrt, ceil
import matplotlib.pyplot as plt

class Drawer:
    def __init__(self, title="", plot_style=""):
        self.title = title
        self.plot_style = plot_style
        self.clear()
        
        self.X_INDEX = 0
        self.Y_INDEX = 1
        self.TITLE_INDEX = 2
        self.XLABEL_INDEX = 3
        self.YLABEL_INDEX = 4
        
    def add(self, x, y, title="", xlabel="x", ylabel="y"):
        self.data.append((x, y, title, xlabel, ylabel))
    
    def clear(self):
        plt.close()
        
        self.data = []
        
    def draw(self):
        l = len(self.data)
        
        fig, axarr = plt.subplots(l, figsize=(5, 3*l), squeeze=False)
        
        for k in range(l):
            x = self.data[k][self.X_INDEX]
            y = self.data[k][self.Y_INDEX]
            title = self.data[k][self.TITLE_INDEX]
            xlabel = self.data[k][self.XLABEL_INDEX]
            ylabel = self.data[k][self.YLABEL_INDEX]
             
            axarr[k, 0].plot(x, y, self.plot_style)
            axarr[k, 0].grid(True)
            axarr[k, 0].set_xlabel(xlabel)
            axarr[k, 0].set_ylabel(ylabel)
            axarr[k, 0].set_title(title)
        
        fig.tight_layout() # To space subplots
    
    def save(self, dest):
        plt.clf()
        
        self.draw()
        plt.savefig(dest, dpi=250)
        
        self.clear()
        
    def show(self):
        plt.clf()
        
        self.draw()
        plt.show()
        
        self.clear()


if __name__ == "__main__":
    pass
    
    
