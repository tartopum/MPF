"""Contain the class to generate a view for differenced data."""

from os.path import join

import matplotlib.pyplot as plt
import pylatex

from mpf.views.abstracts import View
from mpf.models import mongo


__all__ = ('Differencing')


class Differencing(View):
    """Provide a view for differenced data."""

    def __init__(self, path, title, _ids):
        super().__init__(join(path, 'differenced'))

        self.title = title
        self._ids = _ids
        self.cow = mongo.cow(_ids[0])

    def generate(self):
        """Generate the view of differenced production."""

        for _id in self._ids:
            data = mongo.data(_id)
            degree = mongo.settings(_id)['degree']
            
            self.plot(data, degree)
            plt.clf()

    def plot(self, data, degree):
        """Add the plot of differenced data with the degree ``degree``.

        :param data: TODO
        :param degree: The degree with which the data have been differenced.

        :type data: list
        :type degree: int
        """

        days = list(range(degree, degree + len(data)))

        plt.plot(days, data)
        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)

        with self.doc.create(pylatex.Section('Degree = {}'.format(degree))):
            self.add_plot()
