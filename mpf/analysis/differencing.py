"""Contain the class for differencing data."""

from mpf import processors as proc
from mpf import settings as stg


__all__ = ('Differencing')


class Differencing:
    """Difference data."""

    def __init__(self, cow, degree):
        """
        :param cow: The cow the production of to be differenced.
        :param degree: The number of differencings.

        :type cow: int
        :type degree: int
        """

        self.cow = cow
        self.degree = degree

    def save(self, dates, prods):
        """Save the result of the analysis.

        :param dates: The dates corresponding to the differenced productions.
        :param prods: The differenced productions.

        :type dates: list
        :type prods: list
        """

        params = []
        
        for i in range(len(dates)):
            date = dates[i]
            prod = prods[i]

            q_select = 'SELECT id FROM CrudeData WHERE cow = ? AND date = ?'
            fid = stg.model.query(q_select, (self.cow, date))[0][0]

            params.append((fid, prod, self.degree))

        q_insert = 'INSERT INTO DifferencedData VALUES (?, ?, ?)'
        stg.model.querymany(q_insert, params)

    def work(self):
        """Run the analysis."""

        dates = stg.model.dates(self.cow)
        prods = stg.model.prods(self.cow)

        for _ in range(self.degree):
            dates = proc.diff.truncate(dates)
            prods = proc.diff.difference(prods)

        self.save(dates, prods)
