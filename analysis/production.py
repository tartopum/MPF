from os.path import join

from analysis.abstracts import XYAnalysis
from views.linedrawer import LineDrawer
import workers.workers as workers



class ByCons(XYAnalysis):
    """
        TODO
    """

    def __init__(self, cow, selector):
        xgetter = selector.cons
        ygetter = selector.prods
        
        XYAnalysis.__init__(self, cow, xgetter, ygetter)
        
    def work(self, force=False):
        # Crude data
        self.factory.produce(
            worker = workers.Identity(),
            dest = join("productions", "by-cons", str(self.datagroup.name)),
            view = LineDrawer(
                title = str(self.datagroup.name) + "\n\nprod = f(cons)", 
                xlabel = "consumption (kg)", 
                ylabel = "production (L)", 
                plot_style = "bo"
            ),
            force = force
        ).work(self.datagroup)
    

class ByDay(XYAnalysis):
    """
        TODO
    """

    def __init__(self, cow, selector):
        xgetter = selector.lact_days
        ygetter = selector.prods
        
        XYAnalysis.__init__(self, cow, xgetter, ygetter)
        
    def work(self, force=False):
        self.factory.produce(
            worker = workers.Identity(),
            dest = join("productions", "by-day", str(self.datagroup.name)),
            view = LineDrawer(
                title = str(self.datagroup.name) + "\n\nprod = f(day)", 
                xlabel = "day", 
                ylabel = "production (L)"
            ),
            force = force
        ).work(self.datagroup)
        

class ByDayMA(ByDay):
    """
        TODO
    """

    def __init__(self, cow, selector):
        ByDay.__init__(self, cow, selector)
        
    def work(self, force=False):
        steps = [2]
        
        for step in steps:
            self.factory.produce(
                worker = workers.MovingAveraging(step),
                dest = join("productions", "by-day", "moving-averaging", str(self.datagroup.name) + ".step-" + str(step)),
                view = LineDrawer(
                    title = str(self.datagroup.name) + "\n\nprod = f(day)\n\nMA: step = " + str(step), 
                    xlabel = "day", 
                    ylabel = "production (L)"
                ),
                force = force
            ).work(self.datagroup)


class Difference(XYAnalysis):  
    """
        TODO
    """

    def __init__(self, cow, selector):
        xgetter = selector.lact_days
        ygetter = selector.prods
        
        XYAnalysis.__init__(self, cow, xgetter, ygetter)
        
    def work(self, force=False):
        # Crude data
        self.factory.produce(
            worker = workers.Difference(),
            dest = join("productions", "diff", str(self.datagroup.name)),
            view = LineDrawer(
                title = str(self.datagroup.name) + "\n\ny = prod(day + 1) - prod(day)", 
                xlabel = "day", 
                ylabel = "difference (L)"
            ),
            force = force
        ).work(self.datagroup)
