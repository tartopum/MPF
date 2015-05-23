from mpf import processors as proc
from mpf import tools

__all__ = ('MovingAveraging')


class MovingAveraging:
    
    def __init__(self, step):
        self.step = step

    def save(self, cow, dates, prods):
        params = []

        for i in range(len(dates)):
            date = dates[i]
            prod = prods[i]

            q_select = 'SELECT id FROM CrudeData WHERE cow = ? AND date = ?'
            fid = tools.db.query(q_select, (cow, date))[0][0]

            params.append((fid, prod, self.step))
            
        q_insert = 'INSERT INTO SmoothedData VALUES (?, ?, ?)'
        tools.db.querymany(q_insert, params)

    def work(self, cow):
       dates = tools.db.dates(cow)
       dates = proc.ma.truncate(dates, self.step)

       prods = tools.db.prods(cow)
       prods = proc.ma.smooth(prods, self.step)

       self.save(cow, dates, prods)
