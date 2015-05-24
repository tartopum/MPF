"""Contain a class to interact with the database."""

import sqlite3

from mpf import tools


__all__ = ('Database')


class Database:
    """Provide an interface to interact with the database."""

    def __init__(self, path):
        self.connection = sqlite3.connect(path)

    def query(self, sql_query, params=tuple()):
        """Execute the query ``sql_query`` with the parameters ``params``.

        :param sql_query: The SQL query to execute.
        :param params: The parameters to pass to the query.

        :type sql_query: str
        :type params: tuple

        :return: The data returned by the database.
        :rtype: list
        """

        print('{} | {}'.format(sql_query, params))

        cursor = self.connection.cursor()
        data = [row for row in cursor.execute(sql_query, params)]

        self.connection.commit()

        return data

    def querymany(self, sql_query, params):
        """Execute the query ``sql_query`` with the parameters ``params``
        successively.

        :param sql_query: The SQL query to execute.
        :param params: A list of sets of parameters to pass to the query.

        :type sql_query: str
        :type params: tuple
        """

        print('{} | {}'.format(sql_query, params))

        cursor = self.connection.cursor()
        cursor.executemany(sql_query, params)

        self.connection.commit()

    def cows(self):
        """Return the list of the cows."""

        data = self.query('SELECT DISTINCT cow FROM CrudeData')

        return tools.flatten(data)

    def dates(self, cow):
        """Return a list of the dates of ``cow``."""

        data = self.query(
            'SELECT date FROM CrudeData WHERE cow = ? ORDER BY date',
            (cow,)
        )

        return tools.flatten(data)

    def lacts(self, cow):
        """Return the list of the lactations of ``cow``."""

        data = self.query(
            'SELECT DISTINCT lact FROM CrudeData WHERE cow = ? ORDER BY lact',
            (cow,)
        )

        return tools.flatten(data)

    def prods(self, cow):
        """Return the production of ``cow``."""

        data = self.query(
            'SELECT prod FROM CrudeData WHERE cow = ? ORDER BY date',
            (cow,)
        )

        return tools.flatten(data)
