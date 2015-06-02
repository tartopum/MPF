"""Contain the tools for processing the autocorrelation function."""

from statsmodels.tsa.stattools import acf as sm_acf

from mpf.analysis import cache
from mpf.settings import TYPES, LABELS, LONG_MAX_LAGS


__all__ = ('acf')


@cache(TYPES['acf'])
def acf(data, settings):
    """Process the ACF."""

    alpha = settings[LABELS['confint']]['alpha']
    data = data['data']
    nlags = min(LONG_MAX_LAGS, len(data)-1)

    try:
        values, confint = sm_acf(data, nlags=nlags, alpha=alpha)
        confint = [list(i) for i in confint]
    except ValueError:
        values = sm_acf(data, nlags=nlags)
        confint = []

    return {
        LABELS['values']: list(values),
        LABELS['confint']: confint,
    }
