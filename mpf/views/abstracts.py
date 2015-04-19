import os

import matplotlib.pyplot as plt

import pylatex

from mpf.config import FORCE_VIEW

__all__ = ("AbstractView")


class AbstractView:
    
    EXT = "pdf"
    
    def __init__(self):
        root = os.path.dirname(self.FNAME_PATTERN)

        if not os.path.isdir(root):
            os.makedirs(root)

    def add_plot(self):
        self.doc.append(pylatex.command.Command('nobreak'))
        
        with self.doc.create(pylatex.Plt(position="H")) as plot:
            plot.add_plot(plt, width=r'\textwidth')

    def create_doc(self, cow):
        fname = self.FNAME_PATTERN.format(cow.get_key_num())

        if os.path.isfile("{}.{}".format(fname, self.EXT)) and not FORCE_VIEW: 
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
