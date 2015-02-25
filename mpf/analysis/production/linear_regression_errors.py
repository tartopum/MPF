from mpf import processors
from mpf.analysis.production import LinearRegression

__all__ = ("LinRegErrors")



class LinRegErrors:

    def work(self, cow):
        stats = processors.Statistics()
        
        for proportion in LinearRegression.proportions:
            key = ("linreg", "error", proportion)
            errors = [lact.data[key] for lact in cow.get_lacts()]
            
            measures = stats.work(errors)
            
            for k, v in measures.items():
                cow.add_key(("linreg", "errors", proportion, k), v)
