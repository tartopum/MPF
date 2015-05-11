from os.path import join

from mpf.views.production.abstracts import AbstractPlotView
from mpf.analysis import ma
from mpf import config

__all__ = ("MovingAveraging")


class MovingAveraging(AbstractPlotView):

    def __init__(self, cow, step):
       self.DATES_GETTER = ma.MAAnalysis.get_key(key=config.DATES_KEY, step=step)
       self.DAYS_GETTER = ma.MAAnalysis.get_key(key=config.DAYS_KEY, step=step)
       self.PRODS_GETTER = ma.MAAnalysis.get_key(key=config.PRODS_KEY, step=step)
       self.FNAME_PATTERN = join(config.SMOOTHED_PROD_VIEWS_DIR, "{}")
       self.TITLE = "Smoothed data - step = {}".format(step)
       
       AbstractPlotView.__init__(self, cow)
