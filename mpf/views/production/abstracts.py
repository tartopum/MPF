import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pylatex

from mpf.views.abstracts import AbstractView

__all__ = ("AbstractPlotView")


class AbstractPlotView(AbstractView):

    MIN_DAYS_RANGE = 350
    DATE_LABEL = "Date"
    DAY_LABEL = "Day"
    PROD_LABEL = "Production (L)"
    
    def __init__(self, cow):
        AbstractView.__init__(self)
        
        if self.create_doc(cow):
            self.plot(cow)
            self.save()
    
    def draw_lact(self, lact):
        x = lact[self.DAYS_GETTER]
        y = lact[self.PRODS_GETTER]

        plt.plot(x, y)
        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)
        plt.xlim(xmax=max(self.MIN_DAYS_RANGE, max(y)))

        with self.doc.create(pylatex.Section("Lactation {}".format(
            lact.get_key_num()))):
            self.add_plot()

    def draw_lacts(self, cow):
        for lact in sorted(cow.get_lacts()):
            x = lact[self.DAYS_GETTER]
            y = lact[self.PRODS_GETTER]
            
            plt.plot(x, y, label="{}".format(lact.get_key_num()))

        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)
        plt.legend()

        with self.doc.create(pylatex.Section("Lactations")):
            self.add_plot()

    def draw_production(self, cow):
        date_pattern = '%Y-%m-%d'
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter(date_pattern))
        plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

        plt.xlabel(self.DATE_LABEL)
        plt.ylabel(self.PROD_LABEL)

        for lact in sorted(cow.get_lacts()):
            plt.plot(   
                [
                    datetime.datetime.strptime(date, date_pattern).date() 
                    for date in lact[self.DATES_GETTER]
                ],
                lact[self.PRODS_GETTER]
            )

        plt.gcf().autofmt_xdate()

        with self.doc.create(pylatex.Section("Production")):
            self.add_plot()

    def plot(self, cow):
        self.draw_production(cow)
        plt.clf()
    
        self.draw_lacts(cow)
        plt.clf()
    
        for lact in sorted(cow.get_lacts()):
            self.draw_lact(lact)
            plt.clf()
