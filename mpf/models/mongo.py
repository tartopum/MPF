"""Contain a class to interact with the database."""

from pymongo import MongoClient


__all__ = ('Database')


class Database:
    """Provide an interface to interact with the database."""

    def __init__(self, host, port):
        self.client = MongoClient(host, port)
        self.db = self.client.mpf
