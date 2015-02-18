from os.path import join

import mpf.processors as processors
from mpf.analysis.production import LinearRegression

from config import DATA_PATH



class LinRegErrors:

    def __init__(self, cow):
        self.cow = cow
        
    def work(self):
        stats = processors.Statistics()
        
        for proportion in LinearRegression.proportions:
            key = ("linreg", "error", proportion)
            data = [lact.data[key] for lact in self.cow.get_lacts()]
            
            measures = stats.work(data)
            
            for k, v in measures.items():
                self.cow.add_key(("linreg", "error", proportion, k), v)
