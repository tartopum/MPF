import sqlite3

from config import DATABASE_PATH
from drawer import draw, gallery
from manager import Manager
from processor import FourierTransform, LeastSquares, MovingAverage
from selector import Selector

manager = Manager()
selector = Selector(sqlite3.connect(DATABASE_PATH))

def moving_average(x, y):
    step = 3
    obj = MovingAverage(step)
    dest = ""
    
    x, y = manager.work(dest, obj, (x, y))
    
    # Draw
        
def main():
    cows = selector.get_cows()
    
    for cow in cows:
        lactations = selector.get_lactations(cow)
        
        for lactation in lactations:
            pass
        

if __name__ == "__main__":
    main()
