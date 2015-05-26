"""The entry point of the code. Run it to make the analysis work."""

from mpf import analysis
from mpf import views
from mpf.models import mongo
from mpf.settings import LABELS


def main():
    """Launch the analysis."""

    for cow in mongo.cows():
        views.Crude(cow).render()

        analysis.smoothing(
            [LABELS['values']],
            {'values': mongo.identity(cow, LABELS['prods'])['_id']},
            {'step': 2}
        )

        analysis.differencing(
            [LABELS['values']],
            {'values': mongo.identity(cow, LABELS['prods'])['_id']},
            {'degree': 2}
        )


if __name__ == '__main__':
    main()
