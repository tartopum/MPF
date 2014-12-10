from os.path import join

# from drawer import Drawer
from managers import Factory
from selectors import DBSelector

class Drawer:
    def __init__(self, title, plot_style=""):
        pass
        
    def show(self):
        print("show")
        
    def add(self, x, y, title="", xlab="", ylab=""):
        pass

db = DBSelector()
factory = Factory()

def productions(cow):
    # 1. Production by day
    dest = join("productions", "by-day")
    drawer = Drawer("Production by day of " + str(cow))
    
    group = factory.WorkingGroup(cow, dest, drawer)
    group.fill(db.lacts, db.lact_days, db.prods)
    group.work()
    
    ## 1.1 Difference
    dest = join("productions", "diff")
    drawer = Drawer("Production difference of " + str(cow))
    
    group.dest = dest
    group.drawer = drawer
    
    group >> factory.Difference(dest)
    
    ## 1.2 With MA
    step = 2
    dest = join("productions", "by-day", "moving-average", "step-" + str(step))
    title = "Production by day of " + str(cow) + "\n"
    title += "with moving average\n"
    title += "step = " + str(step)"
    drawer = Drawer(title)
    
    group.dest = dest
    group.drawer = drawer
    
    group >> factory.MovingAverage(step, dest)
    
    # 2. Production by cons
    dest = join("productions", "by-cons")
    drawer = Drawer("Production by consumption of " + str(cow), plot_style="bo")
    
    group = factory.WorkingGroup(cow, dest, drawer)
    group.fill(db.lacts, db.lact_days, db.cons)
    group.work()
    
def main():
    for cow in db.cows():
        productions(cow)


if __name__ == "__main__":
    main()
