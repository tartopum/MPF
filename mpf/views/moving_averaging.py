"""Contain the class to generate a view for smoothed data."""

import matplotlib.pyplot as plt
import pylatex

from mpf.views.abstracts import View
from mpf import tools
from mpf import settings as stg


__all__ = ('MovingAveraging')


class MovingAveraging(View):
    """Provide a view for smoothed data."""

    def __init__(self, cow):
        """
        :param cow: The cow the view of is generated.
        :type cow: int
        """

        super().__init__('smoothed')

        self.title = 'Smoothed production'
        self.cow = cow

    def generate(self, steps):
        """Generate the view of smoothed production.

        :param steps: The steps with which the data have been smoothed.
        :type steps: list
        """

        for step in steps:
            self.plot(step)
            plt.clf()

    def plot(self, step):
        """Add the plot of smoothed data with the step ``step``.

        :param step: The step with which the data have been smoothed.
        :type step: int
        """

        data = stg.model.query(
            'SELECT SmoothedData.prod FROM SmoothedData '
            'INNER JOIN CrudeData ON SmoothedData.source = CrudeData.id '
            'WHERE CrudeData.cow = ? AND SmoothedData.step = ? '
            'ORDER BY CrudeData.date',
            (self.cow, step)
        )

        y = tools.flatten(data)
        x = list(range(step, step + len(y)))

        plt.plot(x, y)
        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)

        with self.doc.create(pylatex.Section('Step: {}'.format(step))):
            self.add_plot()
