"""The entry point of the code. Run it to make the analysis work."""

 # TODO
import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages
import statsmodels.api as sm
import matplotlib.pyplot as plt
from time import sleep

from mpf import analysis
from mpf import views
from mpf.models import mongo
from mpf.settings import LABELS


fcast = rpackages.importr('forecast')
tseries = rpackages.importr('tseries')


def smoothing(_id, step):
    return analysis.smoothing({
        LABELS['values']: {'step': step}
    }, {
        'data': _id
    })
     
def differencing(_id, degree):
    return analysis.differencing({
        LABELS['values']: {'degree': degree}
    }, {
        'data': _id
    })

def main():
    """Launch the analysis."""

    for cow in mongo.cows():
        # Crude
        dta = mongo.identity(cow, LABELS['prods'])
        _id = dta['_id']

        views.Crude(_id).render()

        # Smoothing
        smooth_ids = []
        steps = [7, 30]

        for step in steps:
            id_ = smoothing(_id, step)[LABELS['values']]
            smooth_ids.append(id_)

        views.Smoothing('production', 'Smoothed production', 
                        smooth_ids).render()

        # Differencing
        diff_ids = []
        degrees = [1]

        for degree in degrees:
            id_ = differencing(_id, degree)[LABELS['values']]
            diff_ids.append(id_)
            
        views.Differencing('production', 'Differenced production', 
                           diff_ids).render()

        # ACF
        acf_ids = analysis.acf({
            LABELS['values']: {},
            LABELS['confint']: {'alpha': 0.05},
        }, {
            'data': _id,
        })

        views.ACF('production', 'ACF', [acf_ids]).render()

        # PACF
        pacf_ids = analysis.pacf({
            LABELS['values']: {},
            LABELS['confint']: {'alpha': 0.05},
        }, {
            'data': _id,
        })

        views.PACF('production', 'PACF', [pacf_ids]).render()


if __name__ == '__main__':
    main()
