"""Contain the class to generate a view for a correlogram.""" 

import numpy as np
import matplotlib.pyplot as plt
import pylatex

from mpf.views.abstracts import View
from mpf.models import mongo
from mpf import tools
from mpf.settings import LABELS


__all__ = ('Correlogram')


class Correlogram(View):
    """Provide a view for a correlogram."""

    def __init__(self, cow, crude_id, diff_ids, title):
        super().__init__(title.lower())

        self.title = title
        self.cow = cow
        self.crude_id = crude_id
        self.diff_ids = diff_ids

    def get_data(self, _id):
        return mongo.db.analysis.find_one({
            '_id': _id 
        })['data']
        
    def get_confint(self, _id):
        confint = mongo.db.analysis.find_one({
            '_id': _id 
        })['data']

        if not len(confint):
            return []
        else:
            confint = np.array(confint)

            return confint - confint.mean(1)[:,None]

    def generate(self):
        """Generate the view of the correlogram."""

        # Crude
        data = self.get_data(self.crude_id[LABELS['values']])
        confint = self.get_confint(self.crude_id[LABELS['confint']])
        self.plot(data, confint, 'Crude data')

        # Differenced
        for degree in sorted(self.diff_ids.keys()):
            ids = self.diff_ids[degree]

            data = self.get_data(ids[LABELS['values']])
            confint = self.get_confint(ids[LABELS['confint']])

            title = 'Differenced data - degree = {}'.format(degree)
            self.plot(data, confint, title)

    def plot(self, data, confint, title):
        tools.plot_correlogram(data, self.title)
        
        if len(confint):
            plt.fill_between(range(len(data)), confint[:,0], confint[:,1], 
                            alpha=0.25)

        with self.doc.create(pylatex.Section(title)):
            self.add_plot()
            plt.clf()
        
