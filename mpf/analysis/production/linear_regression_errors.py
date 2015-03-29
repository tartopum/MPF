from mpf import processors
from .linear_regression import LinearRegression

__all__ = ("LinRegErrorStats")



class LinRegErrorStats:

    LBL = "errors"

    @classmethod
    def get_key(proportion, k):
        return (
            LinearRegression.label, 
            LinRegErrors.label, 
            proportion, 
            k
        )

    def analyze(self, cow, proportion):
        stats = processors.Statistics()
        
        key = LinearRegression.get_key(
            LinearRegression.error_label, 
            proportion
        )
        
        errors = [cow[lact_key][key] for lact_key in cow.get_lact_keys()]
        
        measures = stats.process(errors)
        
        for k, v in measures.items():
            cow[LinRegErrors.get_key(proportion, k)] = v
