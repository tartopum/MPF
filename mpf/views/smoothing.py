"""Contain the class to generate a view for smoothed data."""

import matplotlib.pyplot as plt
import pylatex

from mpf.views.abstracts import View
from mpf.models import mongo


__all__ = ('Smoothing')


class Smoothing(View):
    """Provide a view for smoothed data."""

    def __init__(self, cow, _id):
        super().__init__('smoothed')

        self.title = 'Smoothed production'
        self._id = _id
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

        prods = mongo.select_field('analysis', {'_id': self._id}, 'data')[0]
        days = list(range(step, step + len(prods)))

        plt.plot(days, prods)
        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)

        with self.doc.create(pylatex.Section('Step = {}:'.format(step))):
            self.add_plot()
