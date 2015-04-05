from random import randint

__all__ = ("process")


def _alea_indexes(begin, end, nb):
    """TODO"""
    
    indexes = []
    i = 0
    
    while i < nb:
        k = randint(begin, end-1)
        
        if k in indexes:
            continue
            
        indexes.append(k)
        i += 1
        
    return indexes

def _data_from_indexes(data, indexes):
    """TODO"""
    
    l = len(data[0])
    
    return [[line[i] for i in range(l) if i in indexes] for line in data]
    
def process(data, percentage):
    """TODO"""
    
    l = len(data[0])
    nb = int(l * percentage / 100)
    indexes = _alea_indexes(0, l, nb)
    
    alea_data = _data_from_indexes(data, indexes)
    
    return alea_data
