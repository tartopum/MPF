"""Contain the class to generate a view for smoothed data."""

from os.path import join

import matplotlib.pyplot as plt
import pylatex

from mpf.views.abstracts import View
from mpf.models import mongo


__all__ = ('Smoothing')


class Smoothing(View):
    """Provide a view for smoothed data."""

    def __init__(self, path, title, _ids):
        super().__init__(join(path, 'smoothed'))

        self.title = title
        self._ids = _ids
        self.cow = mongo.cow(_ids[0])

    def generate(self):
        """Generate the view of smoothed production."""

        for _id in self._ids:
            data = mongo.data(_id)
            step = mongo.settings(_id)['step']

            self.plot(data, step)
            plt.clf()

    def plot(self, data, step):
        """Add the plot of smoothed data with the step ``step``.

        :param data: 
        :param step: The step with which the data have been smoothed.
        
        :type data: list
        :type step: int
        """

        x = list(range(step, step + len(data)))

        plt.plot(x, data)
        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)

        with self.doc.create(pylatex.Section('Step = {}:'.format(step))):
            self.add_plot()
