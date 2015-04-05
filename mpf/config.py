from os.path import join, normpath, realpath

# Paths
ROOT = normpath(join(realpath(__file__), "../.."))

DATA_PATH = join(ROOT, "data")

DATABASE_DIR = join(DATA_PATH, "db")
DATABASE_PATH = join(DATABASE_DIR, "mpf.db")

CACHE_DIR = join(DATA_PATH, "cache")

PROD_DIR = join(DATA_PATH, "production")
