import sqlite3

import managers
import savers
from selector import Selector

from config import DATABASE_PATH

selector = Selector(sqlite3.connect(DATABASE_PATH))
        
def main():
    cows = selector.get_cows()
    
    moving_average_2 = managers.MovingAverage(selector, savers.BasicSaver(), 2)
    
    for cow in cows:
        moving_average_2.work(cow)
        
    moving_average_2.save()
        

if __name__ == "__main__":
    main()
