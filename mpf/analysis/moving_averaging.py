"""Contain the class for smoothing data."""

from mpf import processors as proc
from mpf import settings as stg


__all__ = ('MovingAveraging')


class MovingAveraging:
    """Apply a moving average on data."""

    def __init__(self, cow, step):
        self.cow = cow
        self.step = step

    def save(self, dates, prods):
        """Save the result of the analysis."""

        params = []

        for i in range(len(dates)):
            date = dates[i]
            prod = prods[i]

            q_select = 'SELECT id FROM CrudeData WHERE cow = ? AND date = ?'
            source = stg.model.query(q_select, (self.cow, date))[0][0]

            params.append((source, prod, self.step))

        q_insert = 'INSERT INTO SmoothedData VALUES (NULL, ?, ?, ?)'
        stg.model.querymany(q_insert, params)

    def work(self):
        """Run the analysis."""

        dates = stg.model.dates(self.cow)
        dates = proc.ma.truncate(dates, self.step)

        prods = stg.model.prods(self.cow)
        prods = proc.ma.smooth(prods, self.step)

        self.save(dates, prods)
