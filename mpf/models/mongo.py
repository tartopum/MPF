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

    def analysis(self, _id):
        return self.db.analysis.find({'_id': _id})[0]

    def cow(self, _id):
        while True:
            stg = self.settings(_id)

            try:
                return stg['cow']
            except KeyError:
                _id = self.parents(_id)[0]

    def cows(self):
        """Return the list of the cows."""

        return self.db.crudedata.find().distinct('cow')

    def data(self, _id):
        """Return the data of the analysis ``_id``."""

        return self.analysis(_id)['data']

    def dates(self, cow, lact=None):
        """Return the list of the dates of the cow."""

        return self.select_on_cow(cow, lact, 'date', 'date')

    def days(self, cow, lact):
        """Return the list of the days of the lactation."""

        return self.select_on_cow(cow, lact, 'day', 'day')

    def identity(self, cow, label):
        """Return the identity analysis of ``cow`` labelled ``label``."""

        return self.db.analysis.find_one({
            'type': TYPES['identity'],
            'label': label,
            'settings': {'cow': cow},
        })

    def is_analysis(self, type_, label, parents, settings):
        """Check if the analysis exists."""

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

    def parents(self, _id):
        return self.analysis(_id)['parents']

    def prods(self, cow, lact=None):
        """Return a list with the productions of the cow."""

        return self.select_on_cow(cow, lact, 'prod', 'date')

    def select_field(self, collection, where, field, sort_field=None,
                     order=pymongo.ASCENDING):
        """Select a field in the collection."""

        data = self.db[collection].find(where)

        if sort_field is not None:
            data.sort(sort_field, order)

        return tools.flatten(data, field)

    def select_on_cow(self, cow, lact=None, *args, **kwargs):
        """Select some data of the cow."""

        where = {'cow': cow}

        if lact is not None:
            where['lact'] = lact

        return self.select_field('crudedata', where, *args, **kwargs)

    def settings(self, _id):
        return self.analysis(_id)['settings']
