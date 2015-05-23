import os.path

import matplotlib.pyplot as plt

import pylatex

from mpf.analysis import diff 
from mpf.views.abstracts import AbstractView
from mpf import config

__all__ = ("Differencing")


class Differencing(AbstractView):

    DAY_LABEL = "Day"
    PROD_LABEL = "Production (L)"
    PRODS_GETTER = diff.Difference.get_key(label=config.PRODS_LBL) 
    TITLE = "Differenced production"

    def __init__(self, cow):
        AbstractView.__init__(self, os.path.join("differenced", "{}"))
        
        if self.create_doc(cow):
            self.plot(cow)
            self.save()
    
    def plot_production(self, cow):
        y = cow[self.PRODS_GETTER]
        x = list(range(len(y)))
        
        plt.plot(x, y)
        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)

        with self.doc.create(pylatex.Section("Production")):
            self.add_plot()

    def plot(self, cow):
        self.plot_production(cow)
        plt.clf()
