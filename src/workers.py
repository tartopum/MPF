import processors

class Difference:
    def __init__(self, selector, x_getter, y_getter):
        self.selector = selector
        self.x_getter = x_getter
        self.y_getter = y_getter
        self.processor = processors.Difference()
        
    def work(self, cow):
        data = []
        lacts = self.selector.get_lacts(cow)
        
        for lact in lacts:
            x = self.x_getter(cow, lact)
            y = self.y_getter(cow, lact)
            
            x, y = self.processor.work(x, y)
            
            data.append({
                "lact": lact, 
                "x": x, 
                "y": y
            })
            
        return data

class MovingAverage:
    def __init__(self, selector, x_getter, y_getter, step):
        # 'step' is an integer greater than 1
        self.step = max(1, int(step))
        
        self.processor = processors.MovingAverage(self.step)
        self.selector = selector
        self.x_getter = x_getter
        self.y_getter = y_getter
        
    def work(self, cow):
        data = []
        lacts = self.selector.get_lacts(cow)
        
        for lact in lacts:
            x = self.x_getter(cow, lact)
            y = self.y_getter(cow, lact)
            
            x, y = self.processor.work(x, y)
            
            data.append({
                "lact": lact, 
                "x": x, 
                "y": y
            })
            
        return data

class Productions:
    def __init__(self, selector, x_getter):
        self.selector = selector
        self.x_getter = x_getter
         
    def work(self, cow):
        data = []
        lacts = self.selector.get_lacts(cow)
        
        for lact in lacts:
            x = self.x_getter(cow, lact)
            y = self.selector.get_prods(cow, lact)
            
            data.append({
                "lact": lact, 
                "x": x, 
                "y": y
            })
            
        return data
