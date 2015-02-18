from mpf import processors



class MovingAveraging:

    steps = [2]
    
    def __init__(self, cow):
        self.cow = cow
        
    def work(self):
        for step in MovingAveraging.steps:
            ma = processors.MovingAveraging(step)
            
            for lact in self.cow.get_lacts():
                days_ma, prods_ma = ma.work(lact.days, lact.prods)
                
                lact.add_key(("ma", "days", step), days_ma)
                lact.add_key(("ma", "prods", step), prods_ma)
