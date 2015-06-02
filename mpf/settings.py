"""A collection of variables."""

from os.path import join, normpath, realpath


# Paths
ROOT = normpath(join(realpath(__file__), "../.."))

DATA_DIR = join(ROOT, "data")
VIEWS_DIR = join(DATA_DIR, "views")

# Database
DB_HOST = '127.0.0.1'
DB_PORT = 27017

# Analysis
TYPES = {
    'identity': 0,
    'differencing': 1,
    'smoothing': 2,
    'acf': 3,
    'pacf': 4,
    'arima': 5,
}

LABELS = {
    'values': 0,
    'confint': 1,
    'prods': 2,
    'predict': 3,
}

SHORT_MAX_LAGS = 20
LONG_MAX_LAGS = 400

# Settings
FORCE_CACHE = False 
FORCE_VIEW = False 
