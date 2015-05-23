import sys
from os.path import join
import sqlite3

from mpf.models.db import DBSelector
from mpf.config import DATABASE_PATH



def sanitize(line):
    line = line.replace(",", ".")
    
    return line
    
def check(line):
    try:
        cow = int(line[0])
        date = "-".join(line[3].split("/")[::-1]) # 02/01/2014 to 2014-01-02
        prod = float(line[1])
        cons = float(line[2])
        lac = int(line[5])
        day = int(line[4])
    except:
        return None
    else:
        return (cow, date, prod, cons, lac, day)

def main(path):
    db = DBSelector(DATABASE_PATH)
    q = "INSERT INTO CrudeData VALUES (NULL, ?, ?, ?, ?, ?, ?)"
    
    with open(path, "r") as f:
        lines = f.readlines()
    
    for line in lines:
        data = sanitize(line).split("\t")
        data = check(data)
        
        if data is not None:
            try:
                db.query.execute(q, data)
            except sqlite3.IntegrityError: # If the line already exists
                pass
            else:
                print(data)

if __name__ == "__main__":
    main(sys.argv[1])
