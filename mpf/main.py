from os.path import join
from mpf.models.db import DBSelector
from mpf.analysis import production, views

from mpf.config import DATABASE_PATH, DATA_PATH



def main():
    data = DBSelector(DATABASE_PATH).data()
    
    ma = production.MovingAveraging()
    linreg = production.LinearRegression()
    linreg_errors = production.LinRegErrors()

    # Views
    crude_data_view = views.CrudeData(join(DATA_PATH, "prod"))
    
    for cow_key in data.get_cow_keys():
        cow = data[cow_key]
        
        ma.analyze(cow, step=2)
        
        linreg.analyze(cow, proportion=80)
        
        linreg_errors.analyze(cow, proportion=80)
        
        # Views
        crude_data_view.save(cow)

        break
    
if __name__ == "__main__":
    main()
