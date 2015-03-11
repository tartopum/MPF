from random import randint



class AleaValues:
    """TODO"""

    def __init__(self, percentage):
        """
        TODO
        """
        
        self.percentage = percentage
    
    def _alea_indexes(self, begin, end, nb):
        """
        TODO
        """
        
        indexes = []
        i = 0
        
        while i < nb:
            k = randint(begin, end-1)
            
            if k in indexes:
                continue
                
            indexes.append(k)
            i += 1
            
        return indexes
    
    def _data_from_indexes(self, data, indexes):
        """
        TODO
        """
        
        l = len(data[0])
        
        return [[line[i] for i in range(l) if i in indexes] for line in data]
        
    def process(self, data):
        """
        TODO
        """
        
        l = len(data[0])
        nb = int(l * self.percentage / 100)
        indexes = self._alea_indexes(0, l, nb)
        
        alea_data = self._data_from_indexes(data, indexes)
        
        return alea_data
