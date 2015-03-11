from mpf.analysis import AbstractAnalysis
from mpf import processors

__all__ = ("MovingAveraging")



class MovingAveraging(AbstractAnalysis):
    
    label = "ma"
    days_label = "days"
    prods_label = "prods"
    
    @staticmethod
    def get_key(t, step):
        return (
            MovingAveraging.label, 
            t, 
            step
        )
        
    def analyze(self, cow, step, force=False):
        ma = processors.MovingAveraging(step)
        days_key = MovingAveraging.get_key(MovingAveraging.days_label, step)
        prods_key = MovingAveraging.get_key(MovingAveraging.prods_label, step)
        
        for lact_key in cow.get_lact_keys():
            lact = cow[lact_key]
            
            days_ma = self.cache.get_data(lact, days_key)
            prods_ma = self.cache.get_data(lact, prods_key)
            
            if days_ma is None or prods_ma is None:
                days_ma, prods_ma = ma.process(lact["days"], lact["prods"])
            
            lact[days_key] = days_ma
            lact[prods_key] = prods_ma
            
            self.cache.save_data(lact, days_key, days_ma)
            self.cache.save_data(lact, prods_key, prods_ma)
