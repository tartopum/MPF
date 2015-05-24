"""A collection of variables."""

from os.path import join, normpath, realpath

from mpf.models.sqlite import Database


# Paths
ROOT = normpath(join(realpath(__file__), "../.."))

DATA_DIR = join(ROOT, "data")

DATABASE_DIR = join(DATA_DIR, "db")
DATABASE_PATH = join(DATABASE_DIR, "mpf.db")

VIEWS_DIR = join(DATA_DIR, "views")


# Settings
FORCE_CACHE = False 
FORCE_VIEW = False 

model = Database(DATABASE_PATH)
