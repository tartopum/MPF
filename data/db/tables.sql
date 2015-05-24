CREATE TABLE IF NOT EXISTS CrudeData(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cow INTEGER NOT NULL,
    date DATE NOT NULL,
    prod REAL NOT NULL, -- L
    cons REAL NOT NULL, -- kg
    lact INTEGER NOT NULL,
    day INTEGER NOT NULL,
    UNIQUE (cow, date)
);


CREATE TABLE IF NOT EXISTS SmoothedData(
    fid INTEGER, -- foreign id
    prod REAL NOT NULL,
    step INTEGER,
    FOREIGN KEY(fid) REFERENCES CrudeData(id),
    UNIQUE (fid, step)
);

CREATE TABLE IF NOT EXISTS DifferencedData(
    fid INTEGER, -- foreign id
    prod REAL NOT NULL,
    degree INTEGER,
    FOREIGN KEY(fid) REFERENCES CrudeData(id),
    UNIQUE (fid, degree)
);
