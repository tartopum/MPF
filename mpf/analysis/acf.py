"""Contain the tools for processing the autocorrelation function."""

from statsmodels.tsa.stattools import acf as sm_acf

from mpf.analysis import cache
from mpf.settings import TYPES, LABELS


__all__ = ('acf')


@cache(TYPES['acf'])
def acf(data, settings):
    """Process the ACF."""

    alpha = settings[LABELS['confint']]['alpha']
    data = data['data']

    try:
        values, confint = sm_acf(data, alpha=alpha)
        confint = [list(i) for i in confint]
    except ValueError:
        values = sm_acf(data)
        confint = []

    return {
        LABELS['values']: list(values),
        LABELS['confint']: confint,
    }
