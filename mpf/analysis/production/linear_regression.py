from mpf import processors

__all__ = ("LinearRegression")



class LinearRegression:
    
    proportions = [80]
    
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
        
    def work(self, cow):
        linreg = processors.LinearRegression()
        
        for proportion in LinearRegression.proportions:
            aleavals = processors.AleaValues(proportion)
            
            for lact in cow.get_lacts():
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
