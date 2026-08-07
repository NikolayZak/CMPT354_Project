import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS Customer(
    customerID INTEGER PRIMARY KEY AUTOINCREMENT,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    email VARCHAR(50),
    balance FLOAT
);

CREATE TABLE IF NOT EXISTS Item(
    itemID INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    type VARCHAR(50),
    isAvailable BOOLEAN
);

CREATE TABLE IF NOT EXISTS Records(
    customerID INTEGER,
    itemID INTEGER,
    returnDate DATETIME,
    isReturned BOOLEAN,

    FOREIGN KEY (customerID) REFERENCES Customer(customerID),
    FOREIGN KEY (itemID) REFERENCES Item(itemID),
    PRIMARY KEY (customerID, ItemID)
);

CREATE TABLE IF NOT EXISTS FutureAddition"""


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("library.db")
        cursor = self.conn.cursor()
        cursor.execute(SCHEMA)
        self.conn.commit()