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

        for lact in db_selector.lacts(cow):
            name = "lactation {}".format(lact)
            
            prod_by_cons.add(name, lact)
            prod_by_day.add(name, lact)
            prod_by_day_ma.add(name, lact)
            prod_diff.add(name, lact)
            lin_reg.add(name, lact)
            
        prod_by_cons.work()
        prod_by_day.work()
        prod_by_day_ma.work()
        prod_diff.work()
        lin_reg.work()
        
        break


if __name__ == "__main__":
    main()
