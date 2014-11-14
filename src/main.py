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
    
    group = factory.WorkingGroup(cow, dest, drawer)
    group.fill(
        {
            "prefix": "lactation ",
            "suffix": "",
            "fn": db.lacts
        }, 
        db.lact_days,
        db.prods
    )
    group.work()
    
    ## Difference
    dest = join("productions", "diff", str(cow))
    title = str(cow) + "\n\n"
    title += "y = prod(day + 1) - prod(day)"
    xlabel = "day"
    ylabel = "diff (L)"
    drawer = Drawer(title, xlabel, ylabel)
    
    group.dest = dest
    group.drawer = drawer
    
    group >> factory.Difference(dest)
    
    ## With MA
    step = 2
    dest = join("productions", "by-day", "moving-average", "step-" + str(step), str(cow))
    title = str(cow) + "\n\n"
    title += "prod = f(day)" + "\n\n"
    title += "MA: step = " + str(step)
    xlabel = "day"
    ylabel = "production (L)"
    drawer = Drawer(title, xlabel, ylabel)
    
    group.dest = dest
    group.drawer = drawer
    
    group >> factory.MovingAverage(step, dest)

def production_by_cons(cow):    
    # Crude data
    dest = join("productions", "by-cons", str(cow))
    title = str(cow) + "\n\n"
    title += "prod = f(cons)"
    xlabel = "consumption (kg)"
    ylabel = "production (L)"
    drawer = Drawer(title, xlabel, ylabel, plot_style="bo")
    
    group = factory.WorkingGroup(cow, dest, drawer)
    group.fill(
        {
            "prefix": "lactation ",
            "suffix": "",
            "fn": db.lacts
        }, 
        db.cons,
        db.prods
    )
    group.work()
    
def main():
    for cow in db.cows():
        production_by_day(cow)
        production_by_cons(cow)


if __name__ == "__main__":
    main()
