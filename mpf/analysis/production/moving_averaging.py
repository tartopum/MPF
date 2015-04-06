from mpf.analysis import AbstractAnalysis
from mpf import processors

__all__ = ("MovingAveraging")


class MovingAveraging(AbstractAnalysis):
    
    LBL = "ma"
    
    @classmethod
    def get_key(cls, cat, step):
        return (cls.LBL, cat, step)
    
    @classmethod
    def get_dates_key(cls, step):
        return cls.get_key(cls.DATES_LBL, step)
    
    @classmethod
    def get_days_key(cls, step):
        return cls.get_key(cls.DAYS_LBL, step)
    
    @classmethod
    def get_prods_key(cls, step):
        return cls.get_key(cls.PRODS_LBL, step)
    
    def analyze(self, cow, step):
        ma_dates_key = self.get_dates_key(step)
        ma_days_key = self.get_days_key(step)
        ma_prods_key = self.get_prods_key(step)
        
        for lact_key in cow.get_lact_keys():
            lact = cow[lact_key]
            
            dates_ma = self.cache.get_data(lact, ma_dates_key)
            days_ma = self.cache.get_data(lact, ma_days_key)
            prods_ma = self.cache.get_data(lact, ma_prods_key)
            
            l = len(lact[self.DATES_KEY])
            
            if dates_ma is None:
                dates_ma = lact[self.DATES_KEY][step:l-step]
                self.cache.save_data(lact, ma_dates_key, dates_ma)
            if days_ma is None: 
                days_ma = lact[self.DAYS_KEY][step:l-step]
                self.cache.save_data(lact, ma_days_key, days_ma)
            if prods_ma is None:
                prods_ma = processors.ma.process(lact[self.PRODS_KEY], step)
                self.cache.save_data(lact, ma_prods_key, prods_ma)
            
            lact[ma_dates_key] = dates_ma
            lact[ma_days_key] = days_ma
            lact[ma_prods_key] = prods_ma
