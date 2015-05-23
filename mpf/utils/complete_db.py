import datetime as dt
import sqlite3

from mpf.models.db import DBSelector
from mpf.config import DATABASE_PATH


def get_missing_dates(dates):
    date_set = set(
        dates[0] + dt.timedelta(x) 
        for x in range((dates[-1]-dates[0]).days)
    )
    
    return list(reversed(sorted(date_set - set(dates))))

def main():
    db = DBSelector(DATABASE_PATH)

    q_dates = "SELECT date FROM CrudeData WHERE cow = ? ORDER BY date"
    q_insert = "INSERT INTO CrudeData VALUES (NULL, ?, ?, 0, 0, ?, ?)"
    q_last = "SELECT date, day FROM CrudeData WHERE cow = ? AND lact = ? ORDER BY day DESC LIMIT 1"

    for cow in db.cows():
        print("Completing cow {}...".format(cow))

        dates = [
            dt.datetime.strptime(line[0], "%Y-%m-%d") 
            for line in db.query(q_dates, (cow,))
        ]
        
        missing = get_missing_dates(dates) 

        if missing:
            for lact in reversed(sorted(db.lacts(cow))):
                # The last date and day in database for this lactation
                last_date_str, last_day = db.query(q_last, (cow, lact))[0]
                last_date = dt.datetime.strptime(last_date_str, "%Y-%m-%d") 

                # We start at the last day of the lactation then add the 
                # missing lines till we reach the first day of the lactation
                while last_day > 1:
                    last_day -= 1
                    last_date -= dt.timedelta(1)

                    if last_date in missing:
                        # If day = 1, we'll have a problem of unique key in 
                        # the second loop
                        missing.remove(last_date)

                        db.query(
                            q_insert, 
                            (cow, last_date.strftime("%Y-%m-%d"), lact, last_day)
                        )

                last_date_str, last_day = db.query(q_last, (cow, lact))[0]
                last_date = dt.datetime.strptime(last_date_str, "%Y-%m-%d") 

                # We start at the last day of the lactation then add the 
                # missing lines till we reach the next lactation or the end of 
                # the data if this lactation is the last one
                while (last_date + dt.timedelta(1)) in missing:
                    last_day += 1
                    last_date += dt.timedelta(1)

                    db.query(
                        q_insert, 
                        (cow, last_date.strftime("%Y-%m-%d"), lact, last_day)
                    )


if __name__ == "__main__":
    main()
