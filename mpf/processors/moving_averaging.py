class MovingAveraging:
    """TODO"""

    def __init__(self, step):
        """
        TODO
        """
        
        self.step = step
    
    def work(self, x, y):
        """
        TODO
        """
        
        # Not to alter args
        x = x + []
        y = y + []
        
        x = x[self.step:len(x) - self.step]
        average_y = []
        
        for k in range(self.step, len(y)-self.step):
            # Sum 'step' y before and after the current one,
            # which is y[k]
            s = sum(y[k-self.step:k+self.step+1])
            
            average = float(s) / (2*self.step + 1)
            average_y.append(average) 
            
        y = average_y
        
        return x, y
