"""Contain a class to interact with the database."""

import pymongo

from mpf.settings import TYPES
from mpf import tools


__all__ = ('Database')


class Database:
    """Provide an interface to interact with the database."""

    def __init__(self, host, port):
        self.client = pymongo.MongoClient(host, port)
        self.db = self.client.mpf

    def analysis_type(self, name):
        """"""

        data = self.db.analysistypes.find({'name': name})

        return tools.flatten(data, '_id')

    def cows(self):
        """Return the list of the cows."""

        return self.db.crudedata.find().distinct('cow')

    def data(self, _id):
        """"""
        return self.db.analysis.find({'_id': _id})[0]['data']

    def dates(self, cow, lact=None):
        """Return a list with the dates of the cow."""

        return self.select_on_cow(cow, lact, 'date', 'date') 

    def days(self, cow, lact):
        """"""

        return self.select_on_cow(cow, lact, 'day', 'day') 

    def identity(self, cow, label):
        """"""

        return self.db.analysis.find_one({
            'type': TYPES['identity'],
            'label': label,
            'settings': {'cow': cow},
        })

    def is_analysis(self, type_, label, parents, settings):
        """"""

        return self.db.analysis.find({
            'type': type_,
            'label': label,
            'settings': settings,
            'parents': sorted(parents) 
        }).count()

    def lacts(self, cow):
        """Return the list of the lactations."""

        data = self.db.crudedata.find(
            {'cow': cow}, {'lact': 1, '_id': 0}
        ).sort('lact').distinct('lact')

        return data

    def prods(self, cow, lact=None):
        """Return a list with the productions of the cow."""

        return self.select_on_cow(cow, lact, 'prod', 'date') 

    def select(self, where, field, sort_field, order=pymongo.ASCENDING):
        """TODO"""

        data = self.db.crudedata.find(where).sort(sort_field, order)

        return tools.flatten(data, field)

    def select_on_cow(self, cow, lact=None, *args, **kwargs):
        """TODO"""

        where = {'cow': cow}

        if lact is not None:
            where['lact'] = lact

        return self.select(where, *args, **kwargs)
