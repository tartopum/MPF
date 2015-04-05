import statistics

__all__ = ("process")

FUNCTIONS = {
    "mean": statistics.mean,
    "median": statistics.median,
    "mode": statistics.mode,
    "variance": statistics.variance
}


def process(data):
    """TODO"""
    
    res = {}
    
    for name, fn in FUNCTIONS.items():
        try:
            res[name] = fn(data)
        except statistics.StatisticsError:
            res[name] = None
        
    return res
