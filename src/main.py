from os.path import join

from lib.drawer import Drawer
from lib.managers import Factory
from lib.selectors import DBSelector

db = DBSelector()
factory = Factory()

def production_by_day(cow):
    # Crude data
    dest = join("productions", "by-day", str(cow))
    
    title = str(cow) + "\n\n"
    title += "prod = f(day)"
    
    xlabel="day"
    ylabel="production (L)"
    
    drawer = Drawer(title, xlabel, ylabel)
    
    data = factory.WorkingGroup(cow, dest, drawer)
    data.fill(
        {
            "prefix": "lactation ",
            "suffix": "",
            "fn": db.lacts
        }, 
        db.lact_days,
        db.prods
    )
    
    data.work() # Draw and save crude data
    
    # Difference
    dest = join("productions", "diff", str(cow))
    data.dest = dest
    
    title = str(cow) + "\n\n"
    title += "y = prod(day + 1) - prod(day)"
    
    xlabel = "day"
    ylabel = "diff (L)"
    
    drawer = Drawer(title, xlabel, ylabel)
    data.drawer = drawer
    
    data >> factory.Difference(dest)
    
    # Moving average
    step = 2
    
    dest = join("productions", "by-day", "moving-average", "step-" + str(step), str(cow))
    data.dest = dest
    
    title = str(cow) + "\n\n"
    title += "prod = f(day)" + "\n\n"
    title += "MA: step = " + str(step)
    
    xlabel = "day"
    ylabel = "production (L)"
    
    drawer = Drawer(title, xlabel, ylabel)
    data.drawer = drawer
    
    data >> factory.MovingAverage(step, dest)

def production_by_cons(cow):    
    # Crude data
    dest = join("productions", "by-cons", str(cow))
    
    title = str(cow) + "\n\n"
    title += "prod = f(cons)"
    
    xlabel = "consumption (kg)"
    ylabel = "production (L)"
    
    drawer = Drawer(title, xlabel, ylabel, plot_style="bo")
    
    data = factory.WorkingGroup(cow, dest, drawer)
    data.fill(
        {
            "prefix": "lactation ",
            "suffix": "",
            "fn": db.lacts
        }, 
        db.cons,
        db.prods
    )
    
    data.work()
    
def main():
    for cow in db.cows():
        production_by_day(cow)
        production_by_cons(cow)


if __name__ == "__main__":
    main()
