import os

from mpf.models.db import DBSelector
from mpf.analysis import production, AbstractAnalysis

import mpf.config as config 



def main():
    data = DBSelector(config.DATABASE_PATH).data()

    # Create folder
    if not os.path.isdir(config.PROD_DIR):
        os.makedirs(config.PROD_DIR)

    # Production 
    prod_ma = production.MovingAveraging()
    prod_linreg = production.LinearRegression()
    prod_linreg_stats = production.LinRegErrorStats()
    prod_view = production.View(config.PROD_DIR)
    
    for cow_key in data.get_cow_keys():
        cow = data[cow_key]
        
        # Production 
        prod_ma.analyze(cow, step=2)
        prod_linreg.analyze(cow, proportion=80)
        prod_linreg_stats.analyze(cow, proportion=80)

        prod_view.create_doc(cow)
        prod_view.plot(cow, "Crude data", {
            "dates": AbstractAnalysis.DATES_KEY,
            "days": AbstractAnalysis.DAYS_KEY,
            "prods": AbstractAnalysis.PRODS_KEY
        })
        prod_view.plot(cow, "Smoothed data - step = 2", {
            "dates": prod_ma.get_dates_key(2),
            "days": prod_ma.get_days_key(2),
            "prods": prod_ma.get_prods_key(2)
        })
        prod_view.save()

        break
    
    
if __name__ == "__main__":
    main()
