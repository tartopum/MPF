import matplotlib.pyplot as plt

from mpf.views.drawer import Drawer



__all__ = ["LineDrawer"]



class LineDrawer(Drawer):
    """TODO"""

    def __init__(self, title="", xlabel="x", ylabel="y", plot_style=""):
        """
        TODO
        """
        
        Drawer.__init__(self, title, xlabel, ylabel)
        
        self.plot_style = plot_style
        
    def draw(self):
        """
        TODO
        """
        
        l = len(self.data)
        
        fig = plt.figure(figsize=(4, 2.5*(l+1)))
        
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
