from mpf import processors
from mpf.analysis.production import LinearRegression

__all__ = ("LinRegErrors")



class LinRegErrors:

    label = "errors"

    @staticmethod
    def get_key(proportion, k):
        return (
            LinearRegression.label, 
            LinRegErrors.label, 
            proportion, 
            k
        )

    def work(self, cow):
        stats = processors.Statistics()
        
        for proportion in LinearRegression.proportions:
            key = LinearRegression.get_key(
                LinearRegression.error_label, 
                proportion
            )
            
            errors = [lact[key] for lact in cow.get_lacts()]
            
            measures = stats.work(errors)
            
            for k, v in measures.items():
                cow[LinRegErrors.get_key(proportion, k)] = v
