from mpf.analysis import AbstractAnalysis
from mpf import processors

__all__ = ("MovingAveraging")



class MovingAveraging(AbstractAnalysis):
    
    LBL = "ma"
    
    @classmethod
    def get_key(cls, cat, step):
        return (cls.LBL, cat, step)
    
    def analyze(self, cow, step, force=False):
        ma = processors.MovingAveraging(step)
        ma_days_key = self.get_key(self.DAYS_LBL, step)
        ma_prods_key = self.get_key(self.PRODS_LBL, step)
        
        for lact_key in cow.get_lact_keys():
            lact = cow[lact_key]
            
            days_ma = self.cache.get_data(lact, days_key)
            prods_ma = self.cache.get_data(lact, prods_key)
            
            if days_ma is None or prods_ma is None:
                days_ma, prods_ma = ma.process(lact[self.DAYS_KEY], lact[self.PRODS_KEY])
            
            lact[ma_days_key] = days_ma
            lact[ma_prods_key] = prods_ma
            
            self.cache.save_data(lact, ma_days_key, days_ma)
            self.cache.save_data(lact, ma_prods_key, prods_ma)
