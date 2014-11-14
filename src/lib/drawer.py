from math import sqrt, ceil
import matplotlib.pyplot as plt

class Drawer:
    def __init__(self, title="", xlabel="x", ylabel="y", plot_style=""):
        self.title = title
        self.plot_style = plot_style
        self.xlabel = xlabel
        self.ylabel = ylabel
        
        self.clear()
        
        self.X_INDEX = 0
        self.Y_INDEX = 1
        self.TITLE_INDEX = 2
        
    def add(self, x, y, title=""):
        self.data.append((x, y, title))
    
    def clear(self):
        plt.close()
        
        self.data = []
        
    def draw(self):
        l = len(self.data)
        
        fig = plt.figure(figsize=(5, 3*l))
        
        plt.subplot(l+1, 1, 1)
        plt.text(0.5, 0.5, self.title, ha="center", va="center", fontweight="bold")
        plt.axis('off')
        
        for k in range(l):
            x = self.data[k][self.X_INDEX]
            y = self.data[k][self.Y_INDEX]
            title = self.data[k][self.TITLE_INDEX]
            
            plt.subplot(l+1, 1, k+2) 
            plt.plot(x, y, self.plot_style)
            plt.grid(True)
            plt.xlabel(self.xlabel)
            plt.ylabel(self.ylabel)
            plt.title(title, fontstyle="italic")
        
        fig.tight_layout() # To space subplots
        fig.subplots_adjust(top = 0.975)
    
    def save(self, dest):
        dest += ".png"
        
        plt.clf()
        
        self.draw()
        plt.savefig(dest, dpi=250)
        print(dest + " saved.")
        
        self.clear()
        
    def show(self):
        plt.clf()
        
        self.draw()
        plt.show()
        
        self.clear()


if __name__ == "__main__":
    pass
    
    
