import os
import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from pylatex import Document, Section, Subsection, Plt, Package
from pylatex.command import Command

from mpf.models import DataDict
from mpf.analysis import AbstractAnalysis

__all__ = ("AbstractView, AbstractPlotView")


class AbstractView:
    
    def __init__(self):
        root = os.path.dirname(self.FNAME_PATTERN)

        if not os.path.isdir(root):
            os.makedirs(root)

    def add_plot(self, title):
        with self.doc.create(Subsection(title)):
            self.doc.append(Command('nobreak'))
            
            with self.doc.create(Plt(position="H")) as plot:
                plot.add_plot(plt, width=r'\textwidth')

    def create_doc(self, cow, force=False):
        key = str(AbstractAnalysis.get_key_num(cow.key))
        fname = self.FNAME_PATTERN.format(key)

        if os.path.isfile("{}.pdf".format(fname)) and not force: 
            return False

        self.doc = Document(fname, title="Cow {}".format(key), maketitle=True)
        
        self.doc.packages.append(Package('geometry', options=['left=1cm', 'right=1cm', 'top=1cm', 'bottom=1cm']))
        self.doc.packages.append(Package('float'))
        self.doc.append(Command('pagenumbering', 'gobble'))
    
        return True

    def save(self):
        self.doc.generate_pdf()


class AbstractPlotView(AbstractView):

    MIN_DAYS_RANGE = 350
    DATE_LABEL = "Date"
    DAY_LABEL = "Day"
    PROD_LABEL = "Production (L)"
    
    def draw_lact(self, lact, lact_key):
        x = lact[self.DAYS_GETTER]
        y = lact[self.PRODS_GETTER]

        plt.plot(x, y)
        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)
        plt.xlim(xmax=max(self.MIN_DAYS_RANGE, max(y)))

        self.add_plot("Lactation {}".format(AbstractAnalysis.get_key_num(lact_key)))

    def draw_lacts(self, cow):
        for lact_key in sorted(cow.get_lact_keys()):
            lact = cow[lact_key]

            x = lact[self.DAYS_GETTER]
            y = lact[self.PRODS_GETTER]
            
            plt.plot(x, y, label="{}".format(AbstractAnalysis.get_key_num(lact_key)))

        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)
        plt.legend()

        self.add_plot("All lactations")

    def draw_production(self, cow):
        date_pattern = '%Y-%m-%d'
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter(date_pattern))
        plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

        plt.xlabel(self.DATE_LABEL)
        plt.ylabel(self.PROD_LABEL)

        for lact_key in sorted(cow.get_lact_keys()):
            lact = cow[lact_key]
            
            plt.plot(   
                [
                    datetime.datetime.strptime(date, date_pattern).date() 
                    for date in lact[self.DATES_GETTER]
                ],
                lact[self.PRODS_GETTER]
            )

        plt.gcf().autofmt_xdate()

        self.add_plot("All production")

    def plot(self, cow, *args):
        with self.doc.create(Section(self.TITLE.format(*args))):
            self.draw_production(cow)
            plt.clf()
        
            self.draw_lacts(cow)
            plt.clf()
        
            for lact_key in sorted(cow.get_lact_keys()):
                self.draw_lact(cow[lact_key], lact_key)
                plt.clf()
