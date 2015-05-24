CREATE TABLE IF NOT EXISTS Tables(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    UNIQUE (name)
);

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

INSERT OR IGNORE INTO Tables (name) VALUES ('CrudeData');

CREATE TABLE IF NOT EXISTS SmoothedData(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source INTEGER NOT NULL,
    prod REAL NOT NULL,
    step INTEGER,
    FOREIGN KEY(source) REFERENCES CrudeData(id),
    UNIQUE (source, step)
);

INSERT OR IGNORE INTO Tables (name) VALUES ('SmoothedData');

CREATE TABLE IF NOT EXISTS DifferencedData(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source INTEGER NOT NULL,
    prod REAL NOT NULL,
    degree INTEGER,
    FOREIGN KEY(source) REFERENCES CrudeData(id),
    UNIQUE (source, degree)
);

INSERT OR IGNORE INTO Tables (name) VALUES ('DifferencedData');

CREATE TABLE IF NOT EXISTS ACF(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source INTEGER NOT NULL,
    cow INTEGER NOT NULL,
    acf BLOB,
    confint BLOB,
    FOREIGN KEY(source) REFERENCES Tables(id),
    UNIQUE (cow, source)
);

INSERT OR IGNORE INTO Tables (name) VALUES ('ACF');
