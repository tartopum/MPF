"""Contain the class for smoothing data."""

from mpf import processors as proc
from mpf.analysis import cache
from mpf.settings import TYPES, LABELS


__all__ = ('smoothing')


@cache(TYPES['smoothing'])
def smoothing(data, settings):
    """"""

    data = data['values']
    smoothed = proc.ma.smooth(data, settings['step'])

    return {LABELS['values']: smoothed}
