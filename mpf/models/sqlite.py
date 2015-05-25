"""Contain a class to interact with the database."""

import sqlite3

from mpf import tools


__all__ = ('Database')


class Database:
    """Provide an interface to interact with the database."""

    def __init__(self, path):
        self.connection = sqlite3.connect(path)

    def query(self, q, params=tuple()):
        """Execute the query ``q`` with the parameters ``params``.

        :param q: The SQL query to execute.
        :param params: The parameters to pass to the query.

        :type q: str
        :type params: tuple

        :return: The data returned by the database.
        :rtype: list
        """

        print('{} | {}'.format(q, params))

        cursor = self.connection.cursor()
        data = [row for row in cursor.execute(q, params)]

        self.connection.commit()

        return data

    def querymany(self, q, params):
        """Execute the query ``q`` with the parameters ``params``
        successively.

        :param q: The SQL query to execute.
        :param params: A list of sets of parameters to pass to the query.

        :type sql_query: str
        :type params: tuple
        """

        print('{} | {}'.format(q, params))

        cursor = self.connection.cursor()
        cursor.executemany(q, params)

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

    def tableid(self, table):
        """Return the id of the table ``table``.

        :param table: The name of the table.
        :type table: str

        :return: The id of the table.
        :rtype: int
        """

        data = self.query(
            'SELECT id FROM Tables WHERE name = ?',
            (table,)
        )

        return data[0][0]
