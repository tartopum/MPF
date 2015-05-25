"""The entry point of the code. Run it to make the analysis work."""

import sqlite3

from mpf import analysis
from mpf import views
from mpf import settings as stg


def main():
    """Launch the analysis."""

    for cow in stg.model.cows():
        views.Crude(cow).render()

        try:
            analysis.MovingAveraging(cow, step=2).work()
            analysis.MovingAveraging(cow, step=4).work()
        except sqlite3.IntegrityError:
            pass # TODO: cache
        
        views.MovingAveraging(cow).render([2, 4])

        try:
            analysis.Differencing(cow, degree=1).work()
        except sqlite3.IntegrityError:
            pass # TODO: cache

        views.Differencing(cow).render([1])

        try:
            analysis.Correlogram(cow).work()
        except sqlite3.IntegrityError:
            pass # TODO: cache

        views.Correlogram(cow).render()


if __name__ == '__main__':
    main()
