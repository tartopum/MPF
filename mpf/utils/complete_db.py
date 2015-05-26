"""Complete database with missing dates."""

import datetime as dt
import pymongo

from mpf.models import mongo


def get_last(cow, lact):
    """Get the last date and day of the lactation ``lact`` of the cow
     ``cow``.
    """

    last = list(mongo.db.crudedata.find(
        {'cow': cow, 'lact': lact},
        {'date': 1, 'day': 1, '_id': 0}
    ).sort('day', pymongo.DESCENDING).limit(1))[0]

    return last['date'], last['day']

def get_missing_dates(dates):
    """List the dates missing in ``dates``."""

    date_set = set(
        dates[0] + dt.timedelta(x)
        for x in range((dates[-1]-dates[0]).days)
    )

    return list(reversed(sorted(date_set - set(dates))))

def insert(cow, date, lact, day):
    """Insert a document in the crudedata collection."""

    mongo.db.crudedata.insert({
        'cow': cow,
        'date': date,
        'prod': 0,
        'cons': 0,
        'lact': lact,
        'day': day,
    })

def main():
    """Complete the crudedata collection with missing dates."""

    for cow in mongo.cows():
        print("Completing cow {}...".format(cow))

        dates = mongo.dates(cow)
        missing = get_missing_dates(dates)

        if missing:
            for lact in reversed(mongo.lacts(cow)):
                # The last date and day in database for this lactation
                last_date, last_day = get_last(cow, lact)

                # We start at the last day of the lactation then add the
                # missing lines till we reach the first day of the lactation
                while last_day > 1:
                    last_day -= 1
                    last_date -= dt.timedelta(1)

                    if last_date in missing:
                        # If day = 1, we'll have a problem of unique key in
                        # the second loop
                        missing.remove(last_date)

                        insert(cow, last_date, lact, last_day)

                last_date, last_day = get_last(cow, lact)

                # We start at the last day of the lactation then add the
                # missing lines till we reach the next lactation or the end of
                # the data if this lactation is the last one
                while last_date + dt.timedelta(1) in missing:
                    last_day += 1
                    last_date += dt.timedelta(1)

                    insert(cow, last_date, lact, last_day)


if __name__ == "__main__":
    main()
