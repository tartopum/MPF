import os

import matplotlib.pyplot as plt
import pylatex

from mpf import config

__all__ = ("AbstractView", "AbstractGallery")


class AbstractView:
    
    EXT = "pdf"
    
    def __init__(self, fname_pattern):
        self.fname_pattern = os.path.join(config.VIEWS_DIR, fname_pattern)

    def add_plot(self):
        self.doc.append(pylatex.command.Command('nobreak'))
        
        with self.doc.create(pylatex.Plt(position="H")) as plot:
            plot.add_plot(plt, width=r'\textwidth')

    def create_doc(self, cow):
        fname = self.fname_pattern.format(cow.get_key_num())
        dirname  = os.path.dirname(fname)

        if not os.path.isdir(dirname):
            os.makedirs(dirname)

        if os.path.isfile("{}.{}".format(fname, self.EXT)) and not config.FORCE_VIEW: 
            return False

        self.doc = pylatex.Document(fname, title="Cow {} - {}".format(
            cow.get_key_num(), self.TITLE), maketitle=True)

        self.doc.packages.append(pylatex.Package('geometry', options=[
            'left=1cm', 'right=1cm', 'top=1cm', 'bottom=1cm']))
        self.doc.packages.append(pylatex.Package('float'))
        self.doc.append(pylatex.command.Command('pagenumbering', 'gobble'))

        return True

    def save(self):
        self.doc.generate_pdf()


class AbstractGallery(AbstractView):

    MIN_DAYS_RANGE = 350
    DATE_LABEL = "Date"
    DAY_LABEL = "Day"
    PROD_LABEL = "Production (L)"
    
    def __init__(self, cow, fname_pattern):
        AbstractView.__init__(self, fname_pattern)
        
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
        curr_day = 0

        for lact in sorted(cow.get_lacts()):
            prods = lact[self.PRODS_GETTER]
            n = len(prods)

            plt.plot(   
                list(range(curr_day, curr_day + n)),
                prods
            )

            curr_day += n

        plt.xlabel(self.DAY_LABEL)
        plt.ylabel(self.PROD_LABEL)

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
