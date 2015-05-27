"""Contain the tools for processing the partial autocorrelation function."""

import numpy
from statsmodels.tsa.stattools import pacf as sm_pacf

from mpf.analysis import cache
from mpf.settings import TYPES, LABELS


__all__ = ('pacf')


@cache(TYPES['pacf'])
def pacf(data, settings):
    """Process the PACF."""

    alpha = settings[LABELS['confint']]['alpha']
    data = data['data']

    try:
        values, confint = sm_pacf(data, alpha=alpha)
        confint = [list(i) for i in confint]
    except numpy.linalg.linalg.LinAlgError:
        values = [] 
        confint = []

    return {
        LABELS['values']: list(values),
        LABELS['confint']: confint,
    }
