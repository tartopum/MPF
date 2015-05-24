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

    def __init__(self):
        super().__init__('crude')

        self.title = 'Crude production'

    def generate(self, cow):
        """Generate the view of ``cow``.

        :param cow: The cow the view of is generated.
        :type cow: int
        """

        self.production(cow)
        plt.clf()

        self.lactations(cow)
        plt.clf()

        for lact in stg.model.lacts(cow):
            self.lactation(cow, lact)
            plt.clf()

    def lactation(self, cow, lact):
        """Plot lactation ``lact`` of ``cow``.

        :param cow: The cow.
        :param lact: The lactation of the cow to be plotted.

        :type cow: int
        :type lact: int
        """

        data = stg.model.query(
            'SELECT day, prod FROM CrudeData WHERE cow = ? AND lact = ? '
            'ORDER BY day',
            (cow, lact)
        )

        x = tools.flatten(data, 0)
        y = tools.flatten(data, 1)

        plt.plot(x, y)
        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)
        plt.xlim(xmax=max(self.MIN_DAY_RANGE, max(y)))

        with self.doc.create(pylatex.Section('Lactation {}'.format(lact))):
            self.add_plot()

    def lactations(self, cow):
        """Plot lactations of ``cow`` together.

        :param cow: The cow the lactations of are plotted.
        :type cow: int
        """

        for lact in sorted(stg.model.lacts(cow)):
            data = stg.model.query(
                'SELECT day, prod FROM CrudeData WHERE cow = ? '
                'AND lact = ? ORDER BY day',
                (cow, lact)
            )

            x = tools.flatten(data, 0)
            y = tools.flatten(data, 1)

            plt.plot(x, y, label="{}".format(lact))

        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)
        plt.legend()

        with self.doc.create(pylatex.Section('Lactations')):
            self.add_plot()

    def production(self, cow):
        """Plot production of ``cow`` against days.

        :param cow: The cow the production of is plotted.
        :type cow: int
        """

        y = stg.model.prods(cow)
        x = list(range(len(y)))

        plt.plot(x, y)
        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)

        with self.doc.create(pylatex.Section('Production')):
            self.add_plot()
