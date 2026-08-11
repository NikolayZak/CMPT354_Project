PRAGMA foreign_keys = ON;

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

CREATE TABLE IF NOT EXISTS Record(
    recordID INTEGER PRIMARY KEY AUTOINCREMENT,
    customerID INTEGER,
    itemID INTEGER,
    checkoutDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    returnDate DATETIME DEFAULT NULL,

    FOREIGN KEY (customerID) REFERENCES Customer(customerID),
    FOREIGN KEY (itemID) REFERENCES Item(itemID)
);

CREATE TABLE IF NOT EXISTS FutureAddition(
    futureItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
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

CREATE TABLE IF NOT EXISTS Librarian(
    customerID INTEGER PRIMARY KEY,

    FOREIGN KEY (customerID) REFERENCES Customer(customerID)
);

CREATE TABLE IF NOT EXISTS Volunteer(
    customerID INTEGER,
    Vtime TIME,
    Vdate DATE,
    PRIMARY KEY (customerID, Vtime, Vdate)

    FOREIGN KEY (customerID) REFERENCES Customer(customerID)
);

CREATE TABLE IF NOT EXISTS EventGuest(
    customerID INTEGER,
    eventID INTEGER,

    FOREIGN KEY (customerID) REFERENCES Customer(customerID),
    FOREIGN KEY (eventID) REFERENCES Event(eventID),
    PRIMARY KEY (customerID, eventID)
);

CREATE TRIGGER IF NOT EXISTS prevent_double_borrow
BEFORE INSERT ON Record
WHEN NEW.returnDate IS NULL AND EXISTS (
    SELECT 1
    FROM Record
    WHERE itemID = NEW.itemID
      AND returnDate IS NULL
)
BEGIN
    SELECT RAISE(ABORT, 'Item is already borrowed');
END;