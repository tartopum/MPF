CREATE TABLE IF NOT EXISTS CrudeData(
    cow INTEGER NOT NULL,
    date DATE NOT NULL,
    prod REAL NOT NULL, -- L
    cons REAL NOT NULL, -- kg
    lact INTEGER NOT NULL,
    day INTEGER NOT NULL,
    PRIMARY KEY (cow, date)
);
