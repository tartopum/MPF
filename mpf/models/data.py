__all__ = [
    "Cow",
    "Data",
    "Lact",
    "InvalidChild"
]



class InvalidChild(ValueError):
    pass


class Abstract:

    @staticmethod
    def add_child(cls, obj, key, child, f):
        if not isinstance(child, cls):
            raise InvalidChild("The type of the child is invalid.")
        
        if f:
            obj.data[key] = child
            return
            
        try:
            obj.data[key]
        except KeyError:
            obj.data[key] = child
        else:
            raise InvalidChild("The child {} already exists.".format(key))

    @staticmethod
    def get_children(obj, child_cls):
        return [obj.data[key] for key in obj.data.keys() if child_cls.key_label in key]

    @staticmethod
    def get_key(cls, num):
        return (cls.key_label, num)
        
    @staticmethod
    def items(obj):
        return obj.data.items()    
        

class Lact:
    """A class representing a lactation."""
    
    key_label = "lact"
    
    def __init__(self, num, days, prods, cons):
    
        self.num = num
        self.days = days
        self.prods = prods
        self.cons = cons
        
        self.data = {}

    def __str__(self):
        return str(self.num)

    @classmethod
    def get_key(cls, num): 
        return Abstract.get_key(cls, num)
    
    def add_key(self, key, data, f=False):
        return Abstract.add_child(object, self, key, data, f)
    
    def items(self):
        return Abstract.items(self)
        

class Cow:
    """A class representing a cow."""
    
    key_label = "cow"
    
    def __init__(self, num):
        self.num = num
        self.data = {}
    
    def __str__(self):
        return str(self.num)
    
    @classmethod
    def get_key(cls, num): 
        return Abstract.get_key(cls, num)
    
    def add_key(self, key, data, f=False):
        return Abstract.add_child(object, self, key, data, f)
    
    def add_lact(self, num, lact, f=False): 
        return Abstract.add_child(Lact, self, Lact.get_key(num), lact, f)
        
    def get_lacts(self): 
        return Abstract.get_children(self, Lact)

    def items(self):
        return Abstract.items(self)
        
        
class Data:
    """A class representing data."""

    cow_label = "cow"

    def __init__(self):
        self.data = {}
        
    def add_cow(self, num, cow, f=False): 
        return Abstract.add_child(Cow, self, Cow.get_key(num), cow, f)
        
    def get_cows(self): 
        return Abstract.get_children(self, Cow)
