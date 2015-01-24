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
        
        :Example:
        
        .. code-block:: python
        
            def callable(a, b):
                return [a, b]
                
            data = DataDict()
            
            # data is {}
            
            a = "a"
            b = "b"
            
            getters = [{
                "key": "key",
                "callable": callable,
                "params": (a, b)
            }]
            
            data.get(getters)
            
            # data is {"key": ["a", "b"]}
        """
        
        for getter in getters:
            self[getter["key"]] = getter["callable"](*getter["params"])
