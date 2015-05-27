"""Classes to interact with data."""

from .mongo import Database


__all__ = ('mongo')


mongo = Database('localhost', 27017)
