from os.path import join
import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from pylatex import Document, Section, Subsection, Plt, Package
from pylatex.command import Command

from mpf.models import DataDict
from mpf.analysis import AbstractAnalysis

__all__ = ("View")



class View:
    """TODO"""

    MIN_DAYS_RANGE = 350
    DATE_LABEL = "Date"
    DAY_LABEL = "Day"
    PROD_LABEL = "Production (L)"

    def __init__(self, root):
        self.root = root

    def add_plot(self, title):
        with self.doc.create(Subsection(title)):
            self.doc.append(Command('nobreak'))
            
            with self.doc.create(Plt(position="H")) as plot:
                plot.add_plot(plt, width=r'1\textwidth')

    def create_doc(self, cow):
        key = str(AbstractAnalysis.get_key_num(cow.key))
        fname = join(self.root, key)

        self.doc = Document(fname, title="Cow {}".format(key), maketitle=True)
        
        self.doc.packages.append(Package('geometry', options=['left=1cm', 'right=1cm', 'top=1cm', 'bottom=1cm']))
        self.doc.packages.append(Package('float'))
        self.doc.append(Command('pagenumbering', 'gobble'))

    def draw_lact(self, lact, lact_key, getters):
        x = lact[getters["days"]]
        y = lact[getters["prods"]]

        plt.plot(x, y)
        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)
        plt.xlim(xmax=max(self.MIN_DAYS_RANGE, max(y)))

        self.add_plot("Lactation {}".format(AbstractAnalysis.get_key_num(lact_key)))

    def draw_lacts(self, cow, getters):
        for lact_key in sorted(cow.get_lact_keys()):
            lact = cow[lact_key]

            x = lact[getters["days"]]
            y = lact[getters["prods"]]
            
            plt.plot(x, y, label="{}".format(AbstractAnalysis.get_key_num(lact_key)))

        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)
        plt.legend()

        self.add_plot("Lactations")

    def draw_production(self, cow, getters):
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
                    for date in lact[getters["dates"]]
                ],
                lact[getters["prods"]]
            )

        plt.gcf().autofmt_xdate()

        self.add_plot("The whole production")

    def plot(self, cow, title, getters):
        with self.doc.create(Section(title)):
            self.draw_production(cow, getters)
            plt.clf()
            
            self.draw_lacts(cow, getters)
            plt.clf()
            
            for lact_key in sorted(cow.get_lact_keys()):
                self.draw_lact(cow[lact_key], lact_key, getters)
                plt.clf()

    def save(self):
        self.doc.generate_pdf()
