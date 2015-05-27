"""Classes to interact with data."""

from mpf.settings import DB_HOST, DB_PORT
from .mongo import Database


__all__ = ('mongo')


mongo = Database(DB_HOST, DB_PORT)
