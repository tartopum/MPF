from os.path import join



def by_cons(cow, selector, Drawer, factory, force=False):
    # Drawer
    xlabel = "consumption (kg)"
    ylabel = "production (L)"
    
    drawer = Drawer("", xlabel, ylabel, plot_style="bo")
    
    # Working group
    wg = factory.WorkingGroup(cow, drawer)
    namer = {
        "prefix": "lactation ",
        "suffix": "",
        "getter": selector.lacts
    }
    getters = {
        "x": selector.cons, 
        "y": selector.prods
    }
    wg.fill(namer, getters)
    
    # Crude data
    dest = join("productions", "by-cons", str(cow))
    
    title = str(cow) + "\n\n"
    title += "prod = f(cons)"
    drawer.title = title
    
    wg = factory.Identity(dest, force).work(wg)
    

def by_day(cow, selector, Drawer, factory, force=False):
    # Drawer
    xlabel = "day"
    ylabel = "production (L)"
    
    drawer = Drawer("", xlabel, ylabel)
    
    # Working group
    wg = factory.WorkingGroup(cow, drawer)
    namer = {
        "prefix": "lactation ",
        "suffix": "",
        "getter": selector.lacts
    }
    getters = {
        "x": selector.lact_days, 
        "y": selector.prods
    }
    wg.fill(namer, getters)
    
    # Crude data
    dest = join("productions", "by-day", str(cow))
    
    title = str(cow) + "\n\n"
    title += "prod = f(day)"
    drawer.title = title
    
    wg = factory.Identity(dest, force).work(wg)
    
    # Moving averaging
    steps = [2]
    
    for step in steps:
        dest = join("productions", "by-day", "moving-averaging", str(cow) + ".step-" + str(step))
        
        title = str(cow) + "\n\n"
        title += "prod = f(day)" + "\n\n"
        title += "MA: step = " + str(step)
        drawer.title = title
        
        wg = factory.MovingAveraging(step, dest, force).work(wg)
        

def difference(cow, selector, Drawer, factory, force=False):    
    # Drawer
    xlabel = "day"
    ylabel = "diff (L)"
    
    drawer = Drawer("", xlabel, ylabel)
    
    # Working group
    wg = factory.WorkingGroup(cow, drawer)
    namer = {
        "prefix": "lactation ",
        "suffix": "",
        "getter": selector.lacts
    }
    getters = {
        "x": selector.lact_days, 
        "y": selector.prods
    }
    wg.fill(namer, getters)
    
    # Crude data
    dest = join("productions", "diff", str(cow))
    
    title = str(cow) + "\n\n"
    title += "y = prod(day + 1) - prod(day)"
    drawer.title = title
    
    wg = factory.Difference(dest, force).work(wg)
