"""Contain the tools for differencing data."""

import numpy as np

from mpf import processors as proc
from mpf.analysis import cache
from mpf.settings import TYPES, LABELS


__all__ = ('differencing')


@cache(TYPES['differencing'])
def differencing(data, settings):
    """Difference data."""

    values = data['data']

    for _ in range(settings[LABELS['values']]['degree']):
        values = np.diff(values)

    return {LABELS['values']: values.tolist()}
