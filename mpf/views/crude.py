"""Contain the class to generate a view for crude data."""

import matplotlib.pyplot as plt
import pylatex

from mpf.views.abstracts import View
from mpf import tools
from mpf.settings import mongo


__all__ = ('Crude')


class Crude(View):
    """Provide a view for crude data."""

    MIN_DAY_RANGE = 300

    def __init__(self, cow):
        """
        :param cow: The cow the view of is generated.
        :type cow: int
        """

        super().__init__('crude')

        self.title = 'Crude production'
        self.cow = cow

    def generate(self):
        """Generate the view."""

        self.production()
        plt.clf()

        self.lactations()
        plt.clf()

        for lact in mongo.lacts(self.cow):
            self.lactation(lact)
            plt.clf()

    def lactation(self, lact):
        """Plot lactation ``lact``.

        :param lact: The lactation of the cow to be plotted.
        :type lact: int
        """

        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)
        plt.xlim(xmax=self.MIN_DAY_RANGE)

        prods = mongo.prods(self.cow, lact)
        days = mongo.days(self.cow, lact)
        plt.plot(days, prods)

        with self.doc.create(pylatex.Section('Lactation {}'.format(lact))):
            self.add_plot()

    def lactations(self):
        """Plot lactations of ``cow`` together."""

        for lact in sorted(mongo.lacts(self.cow)):
            prods = mongo.prods(self.cow, lact)
            days = mongo.days(self.cow, lact)

            plt.plot(days, prods, label="{}".format(lact))

        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)
        plt.legend()

        with self.doc.create(pylatex.Section('Lactations')):
            self.add_plot()

    def production(self):
        """Plot production against days."""

        prods = mongo.prods(self.cow)
        days = list(range(len(prods)))

        plt.plot(days, prods)
        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)

        with self.doc.create(pylatex.Section('Production')):
            self.add_plot()
