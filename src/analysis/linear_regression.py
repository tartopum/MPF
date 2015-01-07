from os.path import join



def linear_reg(cow, selector, View, factory, force=False):
    dest = join("linear-regression", str(cow))
    
    wg = factory.WorkingGroup(cow, View())
    namer = {
        "prefix": "lactation ",
        "suffix": "",
        "getter": selector.lacts
    }
    getters = {
        "prods": selector.prods, 
        "cons": selector.cons,
        "lact_days": selector.lact_days
    }
    wg.fill(namer, getters)
    
    wg = factory.LinearRegression(80, dest).work(wg)
    
    return wg
    
    
def linear_reg_stats(cow, selector, View, factory, force=False):
    dest = join("linear-regression", str(cow) + "-stats")
    
    wg = linear_reg(cow, selector, View, factory, force)
    
    wg = factory.Statistics(dest, "diff").work(wg)
