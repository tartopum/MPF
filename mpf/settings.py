"""A collection of variables."""

from os.path import join, normpath, realpath


# Paths
ROOT = normpath(join(realpath(__file__), "../.."))

DATA_DIR = join(ROOT, "data")
VIEWS_DIR = join(DATA_DIR, "views")

# Database
DB_HOST = '127.0.0.1'
DB_PORT = 27017

# Analysis types
TYPES = {
    'identity': 0,
    'differencing': 1,
    'smoothing': 2,
    'acf': 3,
    'pacf': 4,
}

LABELS = {
    'values': 0,
    'confint': 1,
    'prods': 2,
}

# Settings
FORCE_CACHE = False 
FORCE_VIEW = False 
