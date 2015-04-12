from mpf.analysis.abstracts import Analysis
from mpf import processors
from mpf import config

__all__ = ("Smooth", "Truncate")


class MAAnalysis(Analysis):
    
    LBL = "ma"
    
    @classmethod
    def get_keys(cls, step):
        def get_key(cat):
            return (cls.LBL, cat, step)
            
        return {
            config.DATES_KEY: get_key(config.DATES_LBL),
            config.DAYS_KEY: get_key(config.DAYS_LBL),
            config.PRODS_KEY: get_key(config.PRODS_LBL),
            config.CONS_KEY: get_key(config.CONS_LBL)
        }
    
    @classmethod
    def get_key(cls, *args, **kwargs):
        return cls.get_keys(kwargs["step"])[kwargs["key"]]

    @classmethod
    def process(cls, lact, *args, **kwargs):
        key = kwargs["key"]
        step = kwargs["step"]
        
        return cls.processor(lact[key], step)


class Smooth(MAAnalysis):

    processor = processors.ma.smooth
    

class Truncate(MAAnalysis):

    processor = processors.ma.truncate
