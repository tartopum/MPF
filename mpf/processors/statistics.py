import statistics



class Statistics:
    """TODO"""

    mean = statistics.mean
    median = statistics.median
    mode = statistics.mode
    variance = statistics.variance
    
    def __init__(self, functions={}):
        """
        TODO
        """
        
        if functions == {}:
            self.functions = {
                "mean": Statistics.mean,
                "median": Statistics.median,
                "mode": Statistics.mode,
                "variance": Statistics.variance
            }
        else:
            self.functions = functions
    
    def work(self, data):
        """
        TODO
        """
        
        res = {}
        
        for name, fn in self.functions.items():
            try:
                res[name] = fn(data)
            except statistics.StatisticsError:
                res[name] = None
            
        return res
