"""Contain the class to generate a view for the partial autocorrelation 
function.
"""

from mpf.views.correlogram import Correlogram


__all__ = ('PACF')


class PACF(Correlogram):
    """Provide a view for the partial autocorrelation function."""

    def __init__(self, path, title, _ids):
        super().__init__(path, title, _ids, 'pacf')
