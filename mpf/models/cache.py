from os.path import isfile, join
import pickle

from mpf.config import FORCE_CACHE

__all__ = ("Cache")



class Cache:
    """A class to cache data."""
    
    def __init__(self, directory):
        self.directory = directory
        
    def get_data(self, datadict, key):
        filename = self.get_filename(datadict, key)
        path = join(self.directory, filename)
        
        try:
            with open(path, "rb") as f:
                return pickle.load(f)
        except OSError:
            return None
    
    def srepr(self, arg, c):
        if isinstance(arg, str):
            return arg
            
        try:
            return c.join([self.srepr(x, c) for x in arg])
        except TypeError as e: # Catch when for loop fails
            return str(arg) # Not a sequence so just return repr
    
    def get_filename(self, datadict, key):
        keys = list(reversed(datadict.get_parent_keys()))
        keys.append(key)
        
        return self.srepr(keys, "-")  
            
    def save_data(self, datadict, key, data):
        filename = self.get_filename(datadict, key)
        path = join(self.directory, filename)
        
        def save():
            with open(path, "wb") as f:
                pickle.dump(data, f)
                
                print("{} saved.".format(path))
                
        if isfile(path) and FORCE_CACHE or not isfile(path):
            save()
