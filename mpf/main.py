from mpf.models.db import DBSelector
from mpf import analysis
from mpf import config 


def main():
    data = DBSelector(config.DATABASE_PATH).data()

    # Production 
    # crude_prod_view = production.views.crude.View()
    
    for cow in data.get_cows():
        for lact in cow.get_lacts():
            # Moving averaging
            ## X
            analysis.ma.Truncate(lact, key=config.DATES_KEY, step=2)
            analysis.ma.Truncate(lact, key=config.DAYS_KEY, step=2)
            
            ## Y
            analysis.ma.Smooth(lact, key=config.PRODS_KEY, step=2)
            
            # Linear regression
            ## Prods
            key = config.PRODS_LBL
            A = [
                lact[config.CONS_KEY],
                lact[config.DAYS_KEY],
                [lact.get_key_num()] * len(lact[config.DAYS_KEY])
            ]
            B = lact[config.PRODS_KEY]
            
            analysis.linreg.ParamVector(lact, key=key, proportion=80, A=A, B=B)
            analysis.linreg.Error(lact, key=key, proportion=80, A=A, B=B)
            
        # analysis.linreg_stats.Stats(cow, proportion=80)
            
        """
        if crude_prod_view.create_doc(cow):
            crude_prod_view.plot(cow)
            crude_prod_view.save()
        
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

    
if __name__ == "__main__":
    main()
