"""Contain the tools for smoothing data."""

from mpf import processors as proc
from mpf.analysis import cache
from mpf.settings import TYPES, LABELS


__all__ = ('smoothing')


@cache(TYPES['smoothing'])
def smoothing(data, settings):
    """Smooth data."""

    data = data['data']
    values = proc.ma.smooth(data, settings['step'])

    return {LABELS['values']: values}
