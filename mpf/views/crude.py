from os.path import join

from mpf.views.abstracts import AbstractGallery
from mpf import config

__all__ = ("Crude")


class Crude(AbstractGallery):
    
    def __init__(self, cow):
        self.DATES_GETTER = config.DATES_KEY
        self.DAYS_GETTER = config.DAYS_KEY
        self.PRODS_GETTER = config.PRODS_KEY
        self.TITLE = "Crude production"
        
        AbstractGallery.__init__(self, cow, join("crude", "{}"))
