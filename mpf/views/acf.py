"""Contain the class to generate a view for the autocorrelation function."""

from mpf.views.correlogram import Correlogram


__all__ = ('ACF')


class ACF(Correlogram):
    """Provide a view for the partial autocorrelation function."""

    def __init__(self, cow, crude_id, diff_ids):
        super().__init__(cow, crude_id, diff_ids, 'ACF')
