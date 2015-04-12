from mpf.models.cache import Cache
from mpf.config import CACHE_DIR


class Analysis:
    
    cache = Cache(CACHE_DIR)
    
    def __init__(self, lact, *args, **kwargs):
        key_out = self.get_key(*args, **kwargs)
        
        data = self.cache.get_data(lact, key_out)
        
        if data is None:
            data = self.process(lact, *args, **kwargs)
            lact[key_out] = data
            
            self.cache.save_data(lact, key_out)
