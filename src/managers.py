import processors
from savers import BasicSaver

class Manager:
    def __init__(self, selector, saver):
        self.saver = saver
        self.selector = selector
        
    def save(self):
        self.saver.save()

class MovingAverage(Manager):
    def __init__(self, selector, saver, step, rep=1):
        Manager.__init__(self, selector, saver)
        
        # 'step' and 'rep' are integers greater than 1
        self.step = max(1, int(step))
        self.rep = max(1, int(rep))
        
        self.processor = processors.MovingAverage(self.step, self.rep)
        
    def work(self, cow):
        lacts = self.selector.get_lacts(cow)
        
        for lact in lacts:
            x = self.selector.get_lact_days(cow, lact)
            prods = self.selector.get_prods(cow, lact)
            
            self.saver.add((x, prods))
