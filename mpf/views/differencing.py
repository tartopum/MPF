"""Contain the class to generate a view for smoothed data."""

import matplotlib.pyplot as plt
import pylatex

from mpf.views.abstracts import View
from mpf import tools
from mpf import settings as stg


__all__ = ('Differencing')


class Differencing(View):
    """Provide a view for differenced data."""

    def __init__(self, cow):
        """
        :param cow: The cow the view of is generated.
        :type cow: int
        """

        super().__init__('differenced')

        self.title = 'Differenced production'
        self.cow = cow

    def generate(self, degrees):
        """Generate the view of smoothed production.

        :param degrees: The degrees with which the data have been differenced.
        :type degrees: list
        """

        for degree in degrees:
            self.plot(degree)
            plt.clf()

    def plot(self, degree):
        """Add the plot of differenced data with the degree ``degree``.

        :param degree: The degree with which the data have been differenced.
        :type degree: int
        """

        data = stg.model.query(
            'SELECT DifferencedData.prod FROM DifferencedData '
            'INNER JOIN CrudeData ON DifferencedData.source = CrudeData.id '
            'WHERE CrudeData.cow = ? AND DifferencedData.degree = ? '
            'ORDER BY CrudeData.date',
            (self.cow, degree)
        )

        y = tools.flatten(data)
        x = list(range(degree, degree + len(y)))

        plt.plot(x, y)
        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)

        with self.doc.create(pylatex.Section('Degree: {}'.format(degree))):
            self.add_plot()
