from os.path import join

from mpf.views.production.abstracts import AbstractPlotView
from mpf import config

__all__ = ("Crude")


class Crude(AbstractPlotView):
    DATES_GETTER = config.DATES_KEY
    DAYS_GETTER = config.DAYS_KEY
    PRODS_GETTER = config.PRODS_KEY
    FNAME_PATTERN = join(config.CRUDE_PROD_VIEWS_DIR, "{}")
    TITLE = "Crude production"
