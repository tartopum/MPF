"""A collection of variables."""

from os.path import join, normpath, realpath

from mpf.models.mongo import Database


# Paths
ROOT = normpath(join(realpath(__file__), "../.."))

DATA_DIR = join(ROOT, "data")

DATABASE_DIR = join(DATA_DIR, "db")
DATABASE_PATH = join(DATABASE_DIR, "mpf.db")

VIEWS_DIR = join(DATA_DIR, "views")


# Analysis types
IDENTITY = 0
DIFFERENCED = 1
SMOOTHED = 2
ACF = 3
PACF = 4

# Settings
FORCE_CACHE = False 
FORCE_VIEW = False 

mongo = Database('localhost', 27017)
db = mongo.db
