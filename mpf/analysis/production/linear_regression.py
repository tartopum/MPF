from mpf.analysis import AbstractAnalysis
from mpf import processors
from mpf.models import DataDict

__all__ = ("LinearRegression")



class LinearRegression(AbstractAnalysis):
    
    label = "linreg"
    error_label = "error"
    X_label = "X"
    
    @staticmethod
    def get_key(t, proportion):
        return (
            LinearRegression.label,
            t,
            proportion
        )
    
    @staticmethod
    def format_A(data):
        """
        data = [
            [day1, day2, day3],
            [cons1, cons2, cons3]
        ]
        
        A = [
            [1, day1, day1**2, cons1, cons1**2],
            [1, day2, day2**2, cons2, cons2**2],
            [1, day3, day3**2, cons3, cons3**2]
        ]
        """
        
        A = []
        
        for i in range(len(data[0])):
            line = [1] # Offset
            
            for series in data:
                line.append(series[i])
                line.append(series[i]**2)
            
            A.append(line)
            
        return A
        
    def analyze(self, cow, proportion):
        linreg = processors.LinearRegression()
        aleavals = processors.AleaValues(proportion)
        
        error_key = LinearRegression.get_key(
            LinearRegression.error_label,
            proportion
        )
        
        X_key = LinearRegression.get_key(
            LinearRegression.X_label,
            proportion
        )
        
        for lact_key in cow.get_lact_keys():
            lact = cow[lact_key]
            
            X = self.cache.get_data(lact, X_key)
            error = self.cache.get_data(lact, error_key)
            
            if X is None or error is None:
                B = lact["prods"]
                A = LinearRegression.format_A([
                    lact["days"],
                    lact["cons"],
                    [DataDict.get_num(lact_key)] * len(lact["days"])
                ])
                
                A_alea, B_alea = aleavals.process([A, B])
                X = linreg.process(A_alea, B_alea)
                error = linreg.error(X, A, B)
                
            lact[error_key] = error
            lact[X_key] = X
            
            self.cache.save_data(lact, X_key, X)
            self.cache.save_data(lact, error_key, error)
