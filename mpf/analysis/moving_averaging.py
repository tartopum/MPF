from mpf import processors as proc
from mpf import settings as stg 


__all__ = ('MovingAveraging')


class MovingAveraging:
    
    def __init__(self, step):
        self.step = step

    def save(self, cow, dates, prods):
        """Save the result of the analysis of ``cow``."""

        params = []

        for i in range(len(dates)):
            date = dates[i]
            prod = prods[i]

            q_select = 'SELECT id FROM CrudeData WHERE cow = ? AND date = ?'
            fid = stg.model.query(q_select, (cow, date))[0][0]

            params.append((fid, prod, self.step))
            
        q_insert = 'INSERT INTO SmoothedData VALUES (?, ?, ?)'
        stg.model.querymany(q_insert, params)

    def work(self, cow):
        """Run the analysis of ``cow``."""

        dates = stg.model.dates(cow)
        dates = proc.ma.truncate(dates, self.step)

        prods = stg.model.prods(cow)
        prods = proc.ma.smooth(prods, self.step)

        self.save(cow, dates, prods)
