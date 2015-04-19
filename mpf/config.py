from os.path import join, normpath, realpath

# Paths
ROOT = normpath(join(realpath(__file__), "../.."))

DATA_DIR = join(ROOT, "data")

DATABASE_DIR = join(DATA_DIR, "db")
DATABASE_PATH = join(DATABASE_DIR, "mpf.db")

CACHE_DIR = join(DATA_DIR, "cache")

VIEWS_DIR = join(DATA_DIR, "views")
PROD_DIR = join(VIEWS_DIR, "production")
PROD_VIEWS_DIR = join(VIEWS_DIR, "production")
CRUDE_PROD_VIEWS_DIR = join(PROD_VIEWS_DIR, "crude")
SMOOTHED_PROD_VIEWS_DIR = join(PROD_VIEWS_DIR, "smoothed")
LINREG_PROD_VIEWS_DIR = join(PROD_VIEWS_DIR, "linreg")


# Labels/keys
CONS_LBL = "cons"
COW_LBL = "cow"
CRUDE_LBL = "crude"
DATES_LBL = "dates"
DAYS_LBL = "days"
LACT_LBL = "lact"
PRODS_LBL = "prods"

CONS_KEY = (CRUDE_LBL, CONS_LBL)
DATES_KEY = (CRUDE_LBL, DATES_LBL)
DAYS_KEY = (CRUDE_LBL, DAYS_LBL)
PRODS_KEY = (CRUDE_LBL, PRODS_LBL)


# Settings
FORCE_CACHE = False
FORCE_VIEW = False
