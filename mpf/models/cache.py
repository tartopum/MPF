from os.path import isfile, join
import pickle

__all__ = ("Cache")



class Cache:
    """A class to cache data."""
    
    def __init__(self, directory):
        self.directory = directory
        
    def get_data(self, key):
        path = join(self.directory, key)
        
        try:
            with open(path, "r") as f:
                return pickle.load(f)
        except OSError:
            return None
    
    def get_filename(self, d, key):
        parent_keys = reversed(d.get_parent_keys())
        
        filename = [k for k in parent_keys]
        filename.append("-".join(key))
        
        return "-".join(filename)
            
    def save_data(self, d, key, data, force=False):
        filename = self.get_filename(d, key)
        path = join(self.directory, filename)
        
        def save():
            with open(path, "w") as f:
                pickle.dump(data, f)
                
        if isfile(path) and force or not isfile(path):
            save()
