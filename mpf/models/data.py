from mpf import config

__all__ = ("DataDict")



class DataDict(dict):
    
    def __init__(self, key, parent):
        self.key = key
        self.parent = parent

    def __gt__(self, other):
        return self.key > other.key
            
    def __lt__(self, other):
        return self.key < other.key

    def add_child(self, key):
        data = DataDict(key, self)
        self[key] = data
        
        return data

    def concatenate_lacts(self, key):
        lact_keys = sorted(self.get_lact_keys())

        return [val for lact_key in lact_keys for val in self[lact_key][key]]

    def get_cows(self):
        return [self[key] for key in self.get_cow_keys()]

    def get_cow_keys(self):
        return [key for key in self.keys() if config.COW_LBL in key]

    def get_key_num(self):
        return self.key[1]

    def get_lacts(self):
        return [self[key] for key in self.get_lact_keys()]

    def get_lact_keys(self):
        return [key for key in self.keys() if config.LACT_LBL in key]
        
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
