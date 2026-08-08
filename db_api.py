import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS Customer(
    customerID INTEGER PRIMARY KEY AUTOINCREMENT,
    firstName VARCHAR(50),
    lastName VARCHAR(50) DEFAULT NULL,
    email VARCHAR(100) DEFAULT NULL,
    balance INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS Item(
    itemID INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    type VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Records(
    recordID INTEGER PRIMARY KEY AUTOINCREMENT,
    customerID INTEGER,
    itemID INTEGER,
    checkoutDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    returnDate DATETIME DEFAULT NULL,

    FOREIGN KEY (customerID) REFERENCES Customer(customerID),
    FOREIGN KEY (itemID) REFERENCES Item(itemID)
);

CREATE TABLE IF NOT EXISTS FutureAddition(
    name VARCHAR(50) PRIMARY KEY,
    type VARCHAR(50),
    demand INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS Room(
    location VARCHAR(50) PRIMARY KEY,
    capacity INTEGER
);

CREATE TABLE IF NOT EXISTS Event(
    eventID INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    type VARCHAR(50),
    description VARCHAR(300)
);

CREATE TABLE IF NOT EXISTS Booking(
    eventID INTEGER,
    location VARCHAR(50),
    startTime DATETIME,
    endTime DATETIME,

    FOREIGN KEY (location) REFERENCES Room(location),
    FOREIGN KEY (eventID) REFERENCES Event(eventID),
    PRIMARY KEY (location, startTime)
);

CREATE TABLE IF NOT EXISTS EventInterest(
    eventID INTEGER,
    itemType VARCHAR(50),
    
    FOREIGN KEY (eventID) REFERENCES Event(eventID),
    PRIMARY KEY (eventID, itemType)
)"""


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("library.db")
        cursor = self.conn.cursor()
        cursor.execute(SCHEMA)
        self.conn.commit()
