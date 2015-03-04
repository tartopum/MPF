from os.path import isfile, join
import pickle

__all__ = ("Cache")



class Cache:
    """A class to cache data."""
    
    def __init__(self, directory):
        self.directory = directory
        
    def get_data(self, d, key):
        filename = self.get_filename(d, key)
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
    
    def get_filename(self, d, key):
        keys = list(reversed(d.get_parent_keys()))
        keys.append(key)
        
        return self.srepr(keys, "-")  
            
    def save_data(self, d, key, data, force=False):
        filename = self.get_filename(d, key)
        path = join(self.directory, filename)
        
        def save():
            with open(path, "wb") as f:
                pickle.dump(data, f)
                
                print("{} saved.".format(path))
                
        if isfile(path) and force or not isfile(path):
            save()
