"""Contain a class to interact with the database."""

import pymongo

from mpf import tools


__all__ = ('Database')


class Database:
    """Provide an interface to interact with the database."""

    def __init__(self, host, port):
        self.client = pymongo.MongoClient(host, port)
        self.db = self.client.mpf

    def cows(self):
        """Return the list of the cows."""

        return self.db.crudedata.find().distinct('cow')

    def dates(self, cow, lact=None):
        """Return a list with the dates of the cow."""

        return self.select_on_cow(cow, lact, 'date', 'date') 

    def days(self, cow, lact):
        """"""

        return self.select_on_cow(cow, lact, 'day', 'day') 

    def lacts(self, cow):
        """Return the list of the lactations."""

        return self.db.crudedata.find({'cow': cow}).distinct('lact')

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
