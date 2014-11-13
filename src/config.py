from os.path import join, normpath, realpath

# Paths
ROOT = normpath(join(realpath(__file__), "../.."))
DATA_PATH = join(ROOT, "data")
DATABASE_PATH = join(DATA_PATH, "database", "database.db")
