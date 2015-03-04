__all__ = ("DataDict")



class DataDict(dict):
    
    cow_label = "cow"
    lact_label = "lact"
    
    @staticmethod
    def get_num(key):
        return key[1]
    
    def __init__(self, key, parent):
        self.key = key
        self.parent = parent

    def add_child(self, key):
        data = DataDict(key, self)
        self[key] = data
        
        return data

    def get_cow_keys(self):
        return [key for key in self.keys() if DataDict.cow_label in key]

    def get_lact_keys(self):
        return [key for key in self.keys() if DataDict.lact_label in key]
        
    def get_parent_keys(self):
        keys = [self.key]
        parent = self.parent
        
        if self.key is None:
            return []
        elif parent is None:
            return keys
        
        while parent.key is not None:
            keys.append(parent.key)
            
            parent = parent.parent
        
        return keys
