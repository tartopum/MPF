from mpf.models.cache import Cache
from mpf.config import CACHE_DIR

__all__ = ("AbstractAnalysis")



class AbstractAnalysis:
    """An abstract analysis."""
    
    CONS_KEY = ("crude", "cons")
    CONS_LBL = "cons"
    COW_LBL = "cow"
    CRUDE_LBL = "crude"
    DAYS_KEY = ("crude", "days")
    DAYS_LBL = "days"
    LACT_LBL = "lact"
    PRODS_KEY = ("crude", "prods")
    PRODS_LBL = "prods"
    
    @staticmethod
    def get_key_num(key):
        return key[1]
    
    def __init__(self):
        self.cache = Cache(CACHE_DIR)
