from mpf.models.db import DBSelector

from mpf.config import DATABASE_PATH



__all__ = ["data"]


db = DBSelector(DATABASE_PATH)
data = {}

for cow in db.cows():
    data[cow] = db.cow(cow)
    
"""
data = {
    "0001": {
        1: {
            "days": [],
            "prods: [],
            "cons": []
        }
    }
}
"""
