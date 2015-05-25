"""Contain the class to process the autocorrelation functions."""

import pickle
import numpy
import statsmodels.tsa.stattools as sm_tsa_tools

from mpf import settings as stg


__all__ = ('Correlogram')


class Correlogram:
    """Process ACF and PACF."""

    def __init__(self, cow):
        """
        :param cow: The analyzed cow.
        :type cow: int
        """

        self.cow = cow

    def save(self, table, obj, src):
        """Save an analysis.""" 

        obj = pickle.dumps(list(obj)) 

        stg.model.query(
            'INSERT OR IGNORE INTO ' + table + ' VALUES(NULL, ?, ?, ?)', 
            (src, self.cow, obj)
        )

    def work(self):
        """Run the analysis."""

        degree = 1 # TODO
        crude_data = stg.model.prods(self.cow)
        differenced_data = stg.model.query(
            'SELECT DifferencedData.prod FROM DifferencedData '
            'INNER JOIN CrudeData ON DifferencedData.source = CrudeData.id '
            'WHERE DifferencedData.degree = ? AND CrudeData.cow = ? '
            'ORDER BY CrudeData.date',
            (degree, self.cow)
        )

        analysis = [('ACF', sm_tsa_tools.acf), ('PACF', sm_tsa_tools.pacf)]

        for table, proc in analysis:
            try:
                obj = proc(crude_data)
            except numpy.linalg.linalg.LinAlgError:
                obj = []
            finally:
                self.save(table, obj, stg.model.tableid('CrudeData'))

            try:
                obj = proc(differenced_data)
            except numpy.linalg.linalg.LinAlgError:
                obj = []
            finally:
                self.save(table, obj, stg.model.tableid('DifferencedData'))
