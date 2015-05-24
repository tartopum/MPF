"""Contain the class to generate a view for smoothed data."""

import matplotlib.pyplot as plt
import pylatex

from mpf.views.abstracts import View
from mpf import tools
from mpf import settings as stg


__all__ = ('MovingAveraging')


class MovingAveraging(View):
    """Provide a view for smoothed data."""

    def __init__(self):
        super().__init__('smoothed')

        self.title = 'Smoothed production'

    def generate(self, cow, steps):
        """Generate the view of smoothed production of ``cow``.

        :param cow: The cow the view of is generated.
        :param steps: The steps with which the data have been smoothed.

        :type cow: int
        :type steps: list
        """

        for step in steps:
            self.plot(cow, step)
            plt.clf()

    def plot(self, cow, step):
        """Add the plot of smoothed data with the step ``step``.

        :param cow: The cow the view of is generated.
        :param step: The step with which the data have been smoothed.

        :type cow: int
        :type step: int
        """

        data = stg.model.query(
            'SELECT SmoothedData.prod FROM SmoothedData '
            'INNER JOIN CrudeData ON SmoothedData.fid = CrudeData.id '
            'WHERE CrudeData.cow = ? AND SmoothedData.step = ? '
            'ORDER BY CrudeData.date',
            (cow, step)
        )

        y = tools.flatten(data)
        x = list(range(step, step + len(y)))

        plt.plot(x, y)
        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)

        with self.doc.create(pylatex.Section('Step: {}'.format(step))):
            self.add_plot()
