"""The entry point of the code. Run it to make the analysis work."""

from mpf import analysis
from mpf import views
from mpf.models import mongo
from mpf.settings import LABELS


# pylint: disable=too-many-function-args
def main():
    """Launch the analysis."""

    for cow in mongo.cows():
        views.Crude(cow).render()

        smoothing_ids = analysis.smoothing(
            [LABELS['values']],
            {'data': mongo.identity(cow, LABELS['prods'])['_id']},
            {'step': 2}
        )

        views.Smoothing(cow, smoothing_ids[LABELS['values']]).render([2])

        differencing_ids = analysis.differencing(
            [LABELS['values']],
            {'values': mongo.identity(cow, LABELS['prods'])['_id']},
            {'degree': 1}
        )

        views.Differencing(cow, differencing_ids[LABELS['values']]).render([1])


if __name__ == '__main__':
    main()
