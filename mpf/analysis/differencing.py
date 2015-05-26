"""Contain the tools for differencing data."""

from mpf import processors as proc
from mpf.analysis import cache
from mpf.settings import TYPES, LABELS


__all__ = ('differencing')


@cache(TYPES['differencing'])
def differencing(data, settings):
    """Difference data."""

    values = data['values']

    for _ in range(settings['degree']):
        values = proc.diff.difference(values)

    return {LABELS['values']: values}
