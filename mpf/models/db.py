import sqlite3


__all__ = ('Database')


class Database:
    """Provide an interface to interact with the database."""

    def __init__(self, path):
        self.connection = sqlite3.connect(path)
    
    """
    def select(self, table, fields):
        def work(params=tuple(), where=tuple(), orderby=tuple(), limit=-1):
            where = where or {}

            q = 'SELECT '
            q += ', '.join(fields)
            q += ' FROM {}'.format(table)

            if where:
                q += ' WHERE '
                q += ' AND '.join(['{} = ?'.format(field) for field in where])

            if orderby:
                q += ' ORDER BY '
                q += ', '.join(orderby)

            if limit > 0:
                q += ' LIMIT {}'.format(limit)

            return self.query(q, params)

        return work
    """

    def query(self, q, params=tuple()):
        """Execute the query ``q`` with the parameters ``params``."""

        print('{} | {}'.format(q, params))

        cursor = self.connection.cursor()
        data = [row for row in cursor.execute(q, params)]

        self.connection.commit()

        return data

    def querymany(self, q, params):
        """Execute the query ``q`` with the parameters ``params``."""

        print('{} | {}'.format(q, params))

        cursor = self.connection.cursor()
        cursor.executemany(q, params)

        self.connection.commit()

    def cows(self):
        """Return the list of the cows."""

        data = self.query('SELECT DISTINCT cow FROM CrudeData')
 
        return [line[0] for line in data]

    def dates(self, cow):
        """Return a list of the dates of ``cow``."""

        data = self.query(
            'SELECT date FROM CrudeData WHERE cow = ? ORDER BY date',
            (cow,)
        )

        return [line[0] for line in data]

    def prods(self, cow):
        """Return the production of ``cow``."""

        data = self.query(
            'SELECT prod FROM CrudeData WHERE cow = ? ORDER BY date',
            (cow,)
        )

        return [line[0] for line in data]
