from os.path import join

import mpf.processors as processors

from config import DATA_PATH



class MovingAveraging:

    steps = [2]
    
    def __init__(self, cow):
        self.cow = cow
    
    def get_dest(self, step):
        dest = join(DATA_PATH, "production", "moving-averaging")
        dest = join(dest, str(self.cow) + "." + str(step))
        
        return dest
        
    def work(self):
        for step in MovingAveraging.steps:
            dest = self.get_dest(step)
            
            ma = processors.MovingAveraging(step)
            
            for lact in self.cow.get_lacts():
                days_ma, prods_ma = ma.work(lact.days, lact.prods)
                
                lact.add_key(("ma", "days", step), days_ma)
                lact.add_key(("ma", "prods", step), prods_ma)
