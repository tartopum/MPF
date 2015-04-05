from os.path import join, normpath, realpath

# Paths
ROOT = normpath(join(realpath(__file__), "../.."))

DATA_DIR = join(ROOT, "data")

DATABASE_DIR = join(DATA_DIR, "db")
DATABASE_PATH = join(DATABASE_DIR, "mpf.db")

CACHE_DIR = join(DATA_DIR, "cache")

VIEWS_DIR = join(ROOT, "views")
PROD_DIR = join(VIEWS_DIR, "production")
