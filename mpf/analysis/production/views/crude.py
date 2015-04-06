from os.path import join

from mpf.analysis.production.views.abstracts import AbstractPlotView
from mpf.analysis import AbstractAnalysis
from mpf.config import CRUDE_PROD_VIEWS_DIR

__all__ = ("View")


class View(AbstractPlotView):
   DATES_GETTER = AbstractAnalysis.DATES_KEY
   DAYS_GETTER = AbstractAnalysis.DAYS_KEY
   PRODS_GETTER = AbstractAnalysis.PRODS_KEY
   FNAME_PATTERN = join(CRUDE_PROD_VIEWS_DIR, "{}")
   TITLE = "Crude data"
