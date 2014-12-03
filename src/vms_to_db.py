import sys
import sqlite3
from sql import SQLQuery

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
        lac_day = int(line[4])
    except:
        return None
    else:
        return (cow, date, prod, cons, lac, lac_day)

def main():
    query = SQLQuery(sqlite3.connect("../data/database/database.db"))
    q = "INSERT INTO CrudeData VALUES (?, ?, ?, ?, ?, ?)"
    
    lines = sys.stdin.read().split("\n")
    
    for line in lines:
        data = sanitize(line).split("\t")
        data = check(data)
        
        if data is not None:
            query.execute(q, data)

if __name__ == "__main__":
    main()
