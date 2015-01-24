__all__ = ["DataDict"]



class DataDict(dict):
    """A class representing data."""

    def __init__(self):
        pass
        
    def get(self, getters):
        """Add keys by calling some functions.
        
        :param getters: a list of dicts containing the key, the callable 
        and the parameters for the callable
        
        :type getters: list
        """
        
        for getter in getters:
            self[getter["key"]] = getter["callable"](*getter["params"])
