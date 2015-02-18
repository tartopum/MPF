from mpf import processors
from mpf.analysis.production import LinearRegression



class LinRegErrors:

    def __init__(self, cow):
        self.cow = cow
        
    def work(self):
        stats = processors.Statistics()
        
        for proportion in LinearRegression.proportions:
            key = ("linreg", "error", proportion)
            errors = [lact.data[key] for lact in self.cow.get_lacts()]
            
            measures = stats.work(errors)
            
            for k, v in measures.items():
                self.cow.add_key(("linreg", "errors", proportion, k), v)
