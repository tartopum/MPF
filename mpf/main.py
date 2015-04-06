from mpf.models.db import DBSelector
from mpf.analysis import production
import mpf.config as config 


def main():
    data = DBSelector(config.DATABASE_PATH).data()

    # Production 
    crude_prod_view = production.views.crude.View()
    
    for cow_key in data.get_cow_keys():
        cow = data[cow_key]
        
        # Production 
        production.ma.analyze(cow, step=2)
        production.linreg.analyze(cow, proportion=80)
        production.linreg_stats.analyze(cow, proportion=80)
        
        crude_prod_view.create_doc(cow)
        crude_prod_view.plot(cow)
        crude_prod_view.save()
        """
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
        """

        break

    
if __name__ == "__main__":
    main()
