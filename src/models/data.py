class DataDict(dict):
    """A class representing data."""

    def __init__(self):
        pass
        
    def get(self, getters):
        """Add keys by calling some functions.
        
        :param getters: a list of dicts containing the key, the callable 
        and the parameters 
        :type getters: list
        
        :Example:
        
        .. code-block:: python
        
            # A useless function
            def func(cow, lact):
                return [cow, lact]
                
            data = DataDict()
            
            # data is {}
            
            cow = "0001"
            lact = 1
            
            getters = [{
                "key": "key",
                "callable": func,
                "params": (cow, lact)
            }]
            
            data.get(getters)
            
            # data is {"key": ["0001", 1]}
        """
        
        for getter in getters:
            self[getter["key"]] = getter["callable"](*getter["params"])
