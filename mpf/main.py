"""The entry point of the code. Run it to make the analysis work."""

from os.path import join

from mpf import analysis
from mpf import views
from mpf.models import mongo
from mpf.settings import LABELS


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

        acf_ids = analysis.acf({
            LABELS['values']: {},
            LABELS['confint']: {'alpha': 0.05},
        }, {
            'data': _id,
        })

        views.ACF('production', 'ACF', [acf_ids]).render()

        pacf_ids = analysis.pacf({
            LABELS['values']: {},
            LABELS['confint']: {'alpha': 0.05},
        }, {
            'data': _id,
        })

        views.PACF('production', 'PACF', [pacf_ids]).render()

        # Smoothing
        smooth_ids = []
        steps = [7, 30]

        for step in steps:
            id_ = smoothing(_id, step)[LABELS['values']]
            smooth_ids.append(id_)

            # R: TODO
            if step == 7:
                sdta = mongo.data(id_)

        views.Smoothing('production', 'Smoothed production', 
                        smooth_ids).render()

        # Differencing
        diff_ids = []
        acf_ids = []
        pacf_ids = []
        degrees = [1]

        for degree in degrees:
            id_ = differencing(_id, degree)[LABELS['values']]
            diff_ids.append(id_)

            acf_ids.append(analysis.acf({
                LABELS['values']: {},
                LABELS['confint']: {'alpha': 0.05},
            }, {
                'data': id_,
            }))

            pacf_ids.append(analysis.pacf({
                LABELS['values']: {},
                LABELS['confint']: {'alpha': 0.05},
            }, {
                'data': id_,
            }))


        views.Differencing('production', 'Differenced production', 
                           diff_ids).render()

        views.ACF(join('production', 'differenced'), 'ACF', acf_ids).render()

        views.PACF(join('production', 'differenced'), 'PACF', pacf_ids).render()
        

if __name__ == '__main__':
    main()
