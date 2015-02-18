from os.path import join

import mpf.processors as processors

from config import DATA_PATH



class LinearRegression:
    
    proportions = [80]
    
    def __init__(self, cow):
        self.cow = cow
    
    @staticmethod
    def format_A(data):
        A = []
        l = len(data[0])
        
        for i in range(l):
            line = [1] # Offset
            
            for series in data:
                line.append(series[i])
                line.append(series[i]**2)
            
            A.append(line)
            
        return A
    
    def get_dest(self, proportion):
        dest = join(DATA_PATH, "production", "linear-regression")
        dest = join(dest, str(self.cow) + "." + str(proportion))
        
        return dest
        
    def work(self):
        linreg = processors.LinearRegression()
        
        for proportion in LinearRegression.proportions:
            dest = self.get_dest(proportion)
            
            aleavals = processors.AleaValues(proportion)
            
            for lact in self.cow.get_lacts():
                B = lact.prods
                A = LinearRegression.format_A([
                    lact.days,
                    lact.cons,
                    [lact.num] * len(lact.days)
                ])
                
                A_alea, B_alea = aleavals.work([A, B])
                X = linreg.work(A_alea, B_alea)
                error = linreg.error(X, A, B)
                
                lact.add_key(("linreg", "error", proportion), error)
                lact.add_key(("linreg", "X", proportion), X)
