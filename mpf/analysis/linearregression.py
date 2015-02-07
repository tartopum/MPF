from os.path import join

from analysis.abstracts import Analysis, LinRegAnalysis
from views.json import JSONWriter
import workers.workers as workers



class LinearRegression(LinRegAnalysis):
    """
        TODO
    """

    def __init__(self, name, selector):
        LinRegAnalysis.__init__(self, name)
        
        self.selector = selector
        
        self.B_callable = self.selector.prods
    
    def get_A(self, *args):
        A = []
        
        cons = self.selector.cons(*args)
        days = self.selector.lact_days(*args)
        
        l = len(cons)
        
        lact = [args[1] for i in range(l)]
        
        A.append(lact)
        A.append(cons)
        A.append(days)
        
        return A
        
    def work(self, percentage, force=False):
        return self.factory.produce(
            worker = workers.LinearRegression(percentage),
            dest = join("linear-regression", str(self.datagroup.name) + ".perc-" + str(percentage)),
            view = JSONWriter(),
            force = force
        ).work(self.datagroup)
            
            
class Statistics(Analysis):
    """
        TODO
    """
    
    def __init__(self, name, selector):
        Analysis.__init__(self, name)
        
        self.linreg = LinearRegression(name, selector)
    
    def add(self, name, *args):
        self.linreg.add(name, *args)
    
    def work(self, key, percentage, force=False):
        self.datagroup = self.linreg.work(percentage, force)
    
        self.factory.produce(
            worker = workers.Statistics(key),
            dest = join("linear-regression", str(self.datagroup.name) + ".stats-" + key + ".perc-" + str(percentage)),
            view = JSONWriter(),
            force = force
        ).work(self.datagroup)
    
    
