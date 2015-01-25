import json

from mpf.views.abstracts import View



__all__ = ["JSONWriter"]



class JSON(View):
    """TODO"""
    
    def __init__(self):
        self.data = {}
        self.ext = ".json"
        
    def add(self, d):
        """
        TODO
        """
        
        self.data.update(d)
        
    def show(self):
        """
        TODO
        """
        
        print(self.data)
        
    def save(self, dest):
        """
        TODO
        """
        
        dest = self._add_ext(dest)
        
        with open(dest, "w") as f:
            json.dump(self.data, f, indent=4, sort_keys=True)
            
        print(dest + " saved.")
