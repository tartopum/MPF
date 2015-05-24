"""Contain the class to generate a view for crude data."""

import matplotlib.pyplot as plt
import pylatex

from mpf.views.abstracts import View
from mpf import tools
from mpf import settings as stg


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

        for lact in stg.model.lacts(self.cow):
            self.lactation(lact)
            plt.clf()

    def lactation(self, lact):
        """Plot lactation ``lact``.

        :param lact: The lactation of the cow to be plotted.
        :type lact: int
        """

        data = stg.model.query(
            'SELECT day, prod FROM CrudeData WHERE cow = ? AND lact = ? '
            'ORDER BY day',
            (self.cow, lact)
        )

        x = tools.flatten(data, 0)
        y = tools.flatten(data, 1)

        plt.plot(x, y)
        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)
        plt.xlim(xmax=max(self.MIN_DAY_RANGE, max(y)))

        with self.doc.create(pylatex.Section('Lactation {}'.format(lact))):
            self.add_plot()

    def lactations(self):
        """Plot lactations of ``cow`` together."""

        for lact in sorted(stg.model.lacts(self.cow)):
            data = stg.model.query(
                'SELECT day, prod FROM CrudeData WHERE cow = ? '
                'AND lact = ? ORDER BY day',
                (self.cow, lact)
            )

            x = tools.flatten(data, 0)
            y = tools.flatten(data, 1)

            plt.plot(x, y, label="{}".format(lact))

        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)
        plt.legend()

        with self.doc.create(pylatex.Section('Lactations')):
            self.add_plot()

    def production(self):
        """Plot production against days."""

        y = stg.model.prods(self.cow)
        x = list(range(len(y)))

        plt.plot(x, y)
        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)

        with self.doc.create(pylatex.Section('Production')):
            self.add_plot()
