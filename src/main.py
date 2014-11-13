from os.path import join
import sqlite3

from manager import Manager
from selector import Selector

from config import DATABASE_PATH
        
def main():
    db_selector = Selector(sqlite3.connect(DATABASE_PATH))
    db_manager = Manager(db_selector)
    
    cows = db_selector.get_cows()
    
    for cow in cows:
        db_manager.production_by_cons(cow)
        db_manager.production_by_day(cow)
        db_manager.production_diff(cow)


if __name__ == "__main__":
    main()
