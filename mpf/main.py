from mpf.models.db import DBSelector
from mpf.analysis import production
from mpf.views import JSON

from mpf.config import DATABASE_PATH



def main():
    data = DBSelector(DATABASE_PATH).data()
    
    ma = production.MovingAveraging()
    linreg = production.LinearRegression()
    linreg_errors = production.LinRegErrors()
    
    for cow_key in data.get_cow_keys():
        cow = data[cow_key]
        
        ma.analyze(cow, step=2)
        
        linreg.analyze(cow, proportion=80)
        
        linreg_errors.analyze(cow, proportion=80)
        
        # Views
    
        with open("./data_linreg_err.json", "w") as f:    
            JSON.dump(f, data, indent=4)
        
        break

    
if __name__ == "__main__":
    main()
