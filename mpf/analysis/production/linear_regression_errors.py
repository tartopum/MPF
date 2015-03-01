from mpf import processors

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

    def work(self, cow, proportion):
        stats = processors.Statistics()
        
        key = LinearRegression.get_key(
            LinearRegression.error_label, 
            proportion
        )
        
        errors = [lact[key] for lact in cow.get_lacts()]
        
        measures = stats.work(errors)
        
        for k, v in measures.items():
            cow[LinRegErrors.get_key(proportion, k)] = v
