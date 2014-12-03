CREATE TABLE IF NOT EXISTS CrudeData(
    cow INTEGER NOT NULL,
    date DATE NOT NULL,
    prod REAL NOT NULL, -- L
    cons REAL NOT NULL, -- kg
    lac INTEGER NOT NULL,
    lac_day INTEGER NOT NULL,
    PRIMARY KEY (cow, date)
);
