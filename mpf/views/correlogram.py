"""Contain the class to generate a view for a correlogram.""" 

from os.path import join

import numpy as np
import matplotlib.pyplot as plt
import pylatex

from mpf.views.abstracts import View
from mpf.models import mongo
from mpf import tools
from mpf.settings import LABELS, SHORT_MAX_LAGS


__all__ = ('Correlogram')


class Correlogram(View):
    """Provide a view for a correlogram."""

    def __init__(self, path, title, _ids, type_):
        super().__init__(join(path, type_))

        self.title = title
        self._ids = _ids
        self.cow = mongo.cow(_ids[0][LABELS['values']]) 

    def get_confint(self, _id):
        confint = mongo.data(_id) 

        if not len(confint):
            return []
        else:
            confint = np.array(confint)

            return confint - confint.mean(1)[:,None]

    def generate(self):
        """Generate the view of the correlogram."""

        for _id in self._ids:
            data = mongo.data(_id[LABELS['values']])
            confint = self.get_confint(_id[LABELS['confint']])
            
            stg = mongo.settings(
                mongo.parents(_id[LABELS['values']])[0]
            )
            title = ' - '.join(['{} = {}'.format(k, v) for k, v in stg.items()])

            self.plot(data, confint, title)

    def plot(self, data, confint, title):
        with self.doc.create(pylatex.Section(title)):
            for end in (len(data), SHORT_MAX_LAGS):
                dta = data[:end]
                tools.plot_correlogram(dta, self.title)
        
                if len(confint):
                    plt.fill_between(range(len(dta)), confint[:,0][:end], 
                                 confint[:,1][:end], alpha=0.25)

                    self.add_plot()
                    plt.clf()
