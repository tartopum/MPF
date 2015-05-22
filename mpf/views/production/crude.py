from os.path import join

from mpf.views.production.abstracts import AbstractPlotView
from mpf import config

__all__ = ("Crude")


class Crude(AbstractPlotView):
    
    def __init__(self, cow):
        self.DATES_GETTER = config.DATES_KEY
        self.DAYS_GETTER = config.DAYS_KEY
        self.PRODS_GETTER = config.PRODS_KEY
        self.TITLE = "Crude production"
        
        AbstractPlotView.__init__(self, cow, join("crude", "{}"))
