__all__ = ("process")


def process(data, step):
    """TODO"""
    
    smoothed_data = []
    
    for k in range(step, len(data)-step):
        s = sum(data[k-step:k+step+1])
        
        average = float(s) / (2*step + 1)
        smoothed_data.append(average) 
        
    return smoothed_data
