from mpf.models.cache import Cache
from mpf.config import CACHE_DIR


class Analysis:
    
    cache = Cache(CACHE_DIR)
    
    def __init__(self, parent, *args, **kwargs):
        key_out = self.get_key(*args, **kwargs)

        data = self.cache.get_data(parent, key_out)
        
        if data is None:
            data = self.process(parent, *args, **kwargs)
            self.cache.save_data(parent, key_out, data)
            
        parent[key_out] = data
