from mpf.models.db import DBSelector

from mpf.analysis import production

from mpf.config import DATABASE_PATH



def main():
    data = DBSelector(DATABASE_PATH).data()
    
    for cow in data.get_cows():
        production.MovingAveraging(cow).work()
        
        production.LinearRegression(cow).work()
        
        production.LinRegErrors(cow).work()
        
        # Views
        
    
if __name__ == "__main__":
    main()
