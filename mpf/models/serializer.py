import pickle



__all__ = ["Serializer"]



class Serializer:
    """TODO"""
    
    def __init__(self, ext=".data"):
        """
        TODO
        """
        
        self.set_ext(ext)
    
    def _add_ext(self, path):
        """
        TODO
        """
        
        try:
            assert src[len(path)-len(self.ext):] == self.ext
        except AssertionError:
            path += self.ext
        
        return path
    
    def load(self, src):
        """
        TODO
        """
        
        src = self._add_ext(src)
            
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
        
        dest = self._add_ext(dest)
        
        with open(dest, "wb") as f:
            pickle.dump(data, f)
            
        print(dest + " saved.")
        
    def set_ext(self, ext):
        try:
            assert str(ext)[0] == "."
        except AssertionError:
            self.ext = "." + str(ext)
        else:
            self.ext = str(ext)
