"""The entry point of the code. Run it to make the analysis work."""

from mpf import analysis
from mpf import views
from mpf.models import mongo
from mpf.settings import LABELS


def main():
    """Launch the analysis."""

    for cow in mongo.cows():
        prod_id = mongo.identity(cow, LABELS['prods'])['_id']

        views.Crude(cow).render()

        smooth_ids = analysis.smoothing({
            LABELS['values']: {'step': 2}
        }, {
            'data': prod_id
        })

        views.Smoothing(cow, smooth_ids[LABELS['values']]).render([2])

        diff_ids = analysis.differencing({
            LABELS['values']: {'degree': 1}
        }, {
            'data': prod_id
        })

        views.Differencing(cow, diff_ids[LABELS['values']]).render([1])

        acf_ids = analysis.acf({
            LABELS['values']: {},
            LABELS['confint']: {'alpha': 0.05}
        }, {
            'data': prod_id
        })

        acf_diff_ids = analysis.acf({
            LABELS['values']: {},
            LABELS['confint']: {'alpha': 0.05}
        }, {
            'data': diff_ids[LABELS['values']]
        })


if __name__ == '__main__':
    main()
