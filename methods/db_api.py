import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("library.db")
        self.cursor = self.conn.cursor()

        with open("schema.sql", "r") as file:
            schema = file.read()

        self.cursor.executescript(schema)
        self.conn.commit()

    def Close(self):
        self.conn.close()

    def FindItem(self, name, type):
        return

    def BorrowItem(self, itemID):
        return

    def ReturnItem(self, itemID):
        return

    def DonateItem(self, name, type):
        return

    def FindEvent(self, name, date):
        return

    def RegisterForEvent(self, customerID, eventID):
        return

    def Volunteer(self, customerID, time, date):
        return