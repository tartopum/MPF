from models.db import DBSelector
from models.cow import Cow

from analysis import linearregression as linreg
from analysis import production as prod


    
def main():
    db_selector = DBSelector()
    
    for num in db_selector.cows():
        cow = Cow(num)

        prod_by_cons = prod.ByCons(cow, db_selector)
        prod_by_day = prod.ByDay(cow, db_selector)
        prod_by_day_ma = prod.ByDayMA(cow, db_selector)
        prod_diff = prod.Difference(cow, db_selector)
        
        lin_reg = linreg.LinearRegression(cow, db_selector)
        lin_reg_stats = linreg.Statistics(cow, db_selector)

        for lact in db_selector.lacts(cow):
            name = "lactation {}".format(lact)
            
            prod_by_cons.add(name, lact)
            prod_by_day.add(name, lact)
            prod_by_day_ma.add(name, lact)
            prod_diff.add(name, lact)
            lin_reg.add(name, lact)
            lin_reg_stats.add(name, lact)
            
        prod_by_cons.work(force=True)
        prod_by_day.work(force=True)
        prod_by_day_ma.work(force=True)
        prod_diff.work(force=True)
        lin_reg.work(80, force=True)
        lin_reg_stats.work("error", 80, force=True)
        
        break


if __name__ == "__main__":
    main()
