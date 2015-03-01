from mpf.models.db import DBSelector

from mpf.analysis import production

from mpf.config import DATABASE_PATH



def main():
    data = DBSelector(DATABASE_PATH).data()
    
    ma = production.MovingAveraging()
    linreg = production.LinearRegression()
    linreg_errors = production.LinRegErrors()
    
    for cow in data.get_cows():
        ma.work(cow, step=2)
        
        linreg.work(cow, proportion=80)
        
        linreg_errors.work(cow, proportion=80)
        
        # Views
        
    
if __name__ == "__main__":
    main()
