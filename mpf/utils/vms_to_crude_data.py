import sys
from os.path import join
import datetime as dt

import pymongo

import mpf.settings as stg


def sanitize(line):
    line = line.replace(',', '.')
    
    return line
    
def check(line):
    try:
        cow = int(line[0])
        prod = float(line[1])
        cons = float(line[2])
        date = dt.datetime.strptime(line[3], '%d/%m/%Y') # 02/01/2014
        day = int(line[4])
        lact = int(line[5])
    except:
        return None
    else:
        return (cow, date, prod, cons, lact, day)

def main(path):
    values = []

    with open(path, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        data = sanitize(line).split("\t")
        data = check(data)
        
        if data is not None:
            try:
                obj = {
                    'cow': data[0],
                    'date': data[1],
                    'prod': data[2],
                    'cons': data[3],
                    'lact': data[4],
                    'day': data[5],
                }

                stg.db.crudedata.insert_one(obj)
            except pymongo.errors.DuplicateKeyError:
                pass
            else:
                print(obj)


if __name__ == '__main__':
    main(sys.argv[1])
