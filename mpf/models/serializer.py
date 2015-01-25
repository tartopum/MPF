import pickle

from mpf.tools import add_ext



__all__ = ["Serializer"]



class Serializer:
    """TODO"""
    
    def __init__(self, ext=""):
        """
        TODO
        """
        
        self.set_ext(ext)
    
    def load(self, src):
        """
        TODO
        """
        
        src = add_ext(src, self.ext)
            
        try:    
            f = open(src, "rb")
            contents = pickle.load(f)
        except:
            contents = None
        else:
            f.close()
            
        return contents
        
    def save(self, data, dest):
        """
        TODO
        """
        
        dest = add_ext(dest)
        
        with open(dest, "wb") as f:
            pickle.dump(data, f)
            
        print(dest + " saved.")
        
    def set_ext(self, ext):
        """
        TODO
        """
        
        if ext == "":
            self.ext = ext
        else:
            try:
                assert str(ext)[0] == "."
            except AssertionError:
                self.ext = "." + str(ext)
            else:
                self.ext = str(ext)
