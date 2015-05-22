from mpf.models.db import DBSelector
from mpf import analysis
from mpf import views
from mpf import config 


def main():
    data = DBSelector(config.DATABASE_PATH).data()

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
            
        # Differencing
        analysis.diff.Difference(cow, key= config.PRODS_KEY, label=config.PRODS_LBL)

        # Views
        views.production.Crude(cow)
        views.production.MovingAveraging(cow, step=2)

    
if __name__ == "__main__":
    main()
