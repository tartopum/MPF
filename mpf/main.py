"""The starting point of the code. Run it to make the analysis work."""

import sqlite3

from mpf import analysis
from mpf import views
from mpf import settings as stg


def main():
    """Launch the analysis."""

    for cow in stg.model.cows():
        try:
            views.Crude().render(cow)

            analysis.MovingAveraging(step=2).work(cow)
            analysis.MovingAveraging(step=4).work(cow)
            views.MovingAveraging().render(cow, [2, 4])
        except sqlite3.IntegrityError:
            pass # TODO: cache


if __name__ == '__main__':
    main()
