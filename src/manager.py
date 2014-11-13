from os.path import join

from drawer import Drawer
import workers

from config import DATA_PATH

class Manager:
    def __init__(self, selector):
        self.selector = selector
    
    def production_by_cons(self, cow):
        dest = join(DATA_PATH, "productions", "by-cons", "{}".format(cow))
        
        drawer = Drawer(plot_style="bo")
        
        worker = workers.Productions(self.selector, self.selector.get_cons)
        
        data = worker.work(cow)
        
        for line in data:
            x = line["x"]
            y = line["y"]
            title = "lact {}".format(line["lact"])
            drawer.add(x, y, title, xlabel="consumption (kg)", ylabel="production (L)")
          
        drawer.save(dest + ".png")
        print(dest + " saved.")
        
    def production_by_day(self, cow):
        dest = join(DATA_PATH, "productions", "by-day", "{}".format(cow))
        
        drawer = Drawer()
        
        worker = workers.Productions(self.selector, self.selector.get_lact_days)
        
        data = worker.work(cow)
        
        for line in data:
            x = line["x"]
            y = line["y"]
            title = "lact {}".format(line["lact"])
            drawer.add(x, y, title, xlabel="day", ylabel="production (L)")
          
        drawer.save(dest + ".png")
        print(dest + " saved.")
        
    def production_diff(self, cow):
        dest = join(DATA_PATH, "productions", "diff", "{}".format(cow))
        
        drawer = Drawer()
        
        worker = workers.Difference(self.selector, self.selector.get_lact_days, self.selector.get_prods)
        
        data = worker.work(cow)
        
        for line in data:
            x = line["x"]
            y = line["y"]
            title = "lact {}".format(line["lact"])
            drawer.add(x, y, title, xlabel="day", ylabel="diff (L)")
          
        drawer.save(dest + ".png")
        print(dest + " saved.")
