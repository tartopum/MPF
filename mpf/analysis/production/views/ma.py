from os.path import join

from mpf.analysis.production.views.abstracts import AbstractPlotView
from mpf.analysis import AbstractAnalysis
from mpf.analysis.production import MovingAveraging
from mpf.config import SMOOTHED_PROD_VIEWS_DIR

__all__ = ("View")


class View(AbstractPlotView):
   DATES_GETTER = "TODO" 
   DAYS_GETTER = AbstractAnalysis.DAYS_KEY
   PRODS_GETTER = AbstractAnalysis.PRODS_KEY
   FNAME_PATTERN = join(SMOOTHED_PROD_VIEWS_DIR, "{}")
   TITLE = "Smoothed data - step = {}"
