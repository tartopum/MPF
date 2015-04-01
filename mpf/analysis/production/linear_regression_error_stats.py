from mpf.analysis import AbstractAnalysis
from mpf import processors
from .linear_regression import LinearRegression

__all__ = ("LinRegErrorStats")



class LinRegErrorStats(AbstractAnalysis):

    LBL = "errors"

    @classmethod
    def get_key(cls, proportion, k):
        return (
            LinearRegression.LBL, 
            cls.LBL, 
            proportion, 
            k
        )

    def analyze(self, cow, proportion):
        stats = processors.Statistics()
        
        key = LinearRegression.get_key(
            self.PRODS_LBL,
            LinearRegression.ERROR_LBL, 
            proportion
        )
        
        errors = [cow[lact_key][key] for lact_key in cow.get_lact_keys()]
        
        measures = stats.process(errors)
        
        for k, v in measures.items():
            cow[self.get_key(proportion, k)] = v
