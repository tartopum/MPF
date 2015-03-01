from mpf.models import Cache

from mpf.config import CACHE_DIR


__all__ = ("AbstractAnalysis")



class AbstractAnalysis:
    """An abstract analysis."""
    
    def __init__(self):
        self.cache = Cache(CACHE_DIR)
