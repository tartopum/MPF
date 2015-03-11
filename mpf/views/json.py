import json



class JSON:
    """A class representing data as JSON."""
    
    @staticmethod    
    def dump(f, data, indent=False):
        """Save data in ``f``."""
        
        json.dump(JSON.dumps(data), f, indent=indent)
        
    @staticmethod
    def dumps(data):
        """Convert ``data`` into JSON."""
        
        if not isinstance(data, dict):
            return data
        
        return {str(k): JSON.dumps(v) for k, v in data.items()}
