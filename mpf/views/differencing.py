"""Contain the class to generate a view for differenced data."""

import matplotlib.pyplot as plt
import pylatex

from mpf.views.abstracts import View
from mpf.models import mongo


__all__ = ('Differencing')


class Differencing(View):
    """Provide a view for differenced data."""

    def __init__(self, cow, _id):
        super().__init__('differenced')

        self.title = 'Differenced production'
        self._id = _id
        self.cow = cow

    def generate(self, degrees):
        """Generate the view of differenced production.

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

        prods = mongo.select_field('analysis', {'_id': self._id}, 'data')[0]
        days = list(range(degree, degree + len(prods)))

        plt.plot(days, prods)
        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)

        with self.doc.create(pylatex.Section('Degree = {}'.format(degree))):
            self.add_plot()
