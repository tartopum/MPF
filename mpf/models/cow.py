__all__ = ["Cow"]



class Cow:
    """TODO"""
    
    def __init__(self, num):
        """
        TODO
        """
        
        self.num = num
        
    def __int__(self):
        """
        TODO
        """
        
        return self.num
        
    def __str__(self):
        """
        TODO
        """
        
        num = str(self.num)
        
        return "0" * (4 - len(num)) + num
