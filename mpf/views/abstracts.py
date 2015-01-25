from mpf.tools import add_ext



__all__ = ["View"]



class View:
    """An abstract view class."""
    
    def __init__(self):
        pass
        
    def _add_ext(self, path):
        """
        TODO
        """
        
        return add_ext(path, self.ext)
