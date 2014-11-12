from math import sqrt, ceil
from PIL import Image
import matplotlib.pyplot as plt

class Drawer():
    def __init__(self):
        pass
    
    def draw(func):
        def wrapper(title, xlabel, ylabel):
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.grid(True)
            plt.title(title)
                
            func()
            
            plt.clf()
            
        return wrapper
    
    def gallery(self, data, dest):
            
        plt.savefig(dest)
        plt.clf()
    
    @draw    
    def save(self, dest, title="", xlabel="Days", ylabel="Production (L)"):
        plt.savefig(dest)
    
    @draw    
    def show(self, title="", xlabel="Days", ylabel="Production (L)"):
        plt.show()
