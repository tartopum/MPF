__all__ = ("smooth", "truncate")


def truncate(data, step):
    """TODO"""
    
    return data[step:-step]
    
def smooth(data, step):
    """TODO"""
    
    width = 2*step + 1
    smoothed_data = []
    
    for k in range(len(data)-2*step):
        s = sum(data[k:k+width])
        
        average = float(s) / width
        smoothed_data.append(average) 
        
    return smoothed_data
