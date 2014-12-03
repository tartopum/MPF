from os.path import join, normpath, realpath

# Paths
ROOT = normpath(join(realpath(__file__), "../.."))
DATA_PATH = join(ROOT, "data")
# DATABASE_PATH = join(DATA_PATH, "database", "database.db")
DATABASE_PATH = normpath(join(ROOT, "..", "..", "mpf.db"))
SQL_PATH = join(DATA_PATH, "database", "sql")
