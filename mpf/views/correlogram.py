"""Contain the class to generate a view for smoothed data."""

import matplotlib.pyplot as plt
import pylatex
import pickle

from mpf.views.abstracts import View
from mpf import tools
from mpf import settings as stg


__all__ = ('Correlogram')


class Correlogram(View):
    """Provide a view for autocorrelation function."""

    def __init__(self, cow):
        """
        :param cow: The cow the view of is generated.
        :type cow: int
        """

        super().__init__('correlogram')

        self.title = 'Correlograms'
        self.cow = cow

    def generate(self):
        """Generate the view of autocorrelation function."""

        tables = ['ACF', 'PACF']
        sources = ['CrudeData', 'DifferencedData']

        for table in tables:
            for source in sources:
                data = stg.model.query(
                    'SELECT coefficients FROM ' + table + ' '
                    'WHERE cow = ? AND source = ?',
                    (self.cow, stg.model.tableid(source))
                )

                y = pickle.loads(tools.flatten(data)[0])

                tools.plot_correlogram(y, table)

                with self.doc.create(pylatex.Section(table + ' - ' + source)):
                    self.add_plot()
                    plt.clf()
