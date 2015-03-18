from os.path import join

import matplotlib.pyplot as plt
from pylatex import Document, Plt

from mpf.models import DataDict

__all__ = ("CrudeData")



class CrudeData:
    """TODO"""

    def __init__(self, root):
        self.root = root

    def save(self, cow):
        title = str(DataDict.get_num(cow.key))
        fname = join(self.root, title)

        doc = Document(fname, title=title)
        
        for lact_key in cow.get_lact_keys():
            lact = cow[lact_key]

            x = lact["days"]
            y = lact["prods"]

            plt.plot(x, y)
            plt.xlabel("Days")
            plt.ylabel("Production")

            with doc.create(Plt(position="htbp")) as plot:
                plot.add_plot(plt)
                plot.add_caption("Lactation {}".format(DataDict.get_num(lact_key)))

            plt.clf()
        
        doc.generate_pdf()
