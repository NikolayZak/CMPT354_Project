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
        self.cursor.execute("""
            SELECT *
            FROM Item
            WHERE name LIKE ? AND type LIKE ?
        """, (f"%{name}%", f"%{type}%"))

        return self.cursor.fetchall()
    
    def BorrowItem(self, customerID, itemID):
        try:
            self.cursor.execute("""
                INSERT INTO Record (customerID, itemID)
                VALUES (?, ?)""", (customerID, itemID))

            self.conn.commit()
            print("Successfully borrowed the item!")
            return

        except sqlite3.IntegrityError:
            self.conn.rollback()
            print(f"Unable to borrow item")
            return

    def ReturnItem(self, itemID):
        self.cursor.execute("""
            UPDATE Record
            SET returnDate = CURRENT_TIMESTAMP
            WHERE itemID = ?
            AND returnDate IS NULL
        """, (itemID,))

        # Case: Not being borrowed
        if self.cursor.rowcount == 0:
            self.conn.rollback()
            print("Item is not currently borrowed.")
            return

        self.conn.commit()
        print("Item has been returned.")

    def DonateItem(self, name, type):
        self.cursor.execute("""
            INSERT INTO Item (name, type)
            VALUES (?, ?)
        """, (name, type))

        self.conn.commit()
        print("Your item has been donated!")

    def FindEvent(self, name):
        self.cursor.execute("""
        SELECT *
        FROM Event
        WHERE name LIKE ?""",
          (f"%{name}%"))
        return self.cursor.fetchall()

    def RegisterForEvent(self, customerID, eventID):
        try:
            self.cursor.execute("""
                INSERT INTO EventGuest (customerID, eventID)
                VALUES (?, ?)
            """, (customerID, eventID))

            self.conn.commit()
            print("You have been registered!")
            return

        except sqlite3.IntegrityError:
            self.conn.rollback()
            print("Unable to register you for the event")
            return

    def Volunteer(self, customerID, time, date):
        try:
            self.cursor.execute("""
                INSERT INTO Volunteer (customerID, Vtime, Vdate)
                VALUES (?, ?, ?)""",
                (customerID, time, date))

            self.conn.commit()
            print("You have been registered to volunteer!")
        except sqlite3.IntegrityError:
            self.conn.rollback()
            print("Unable to volunteer at that time")
            return

    def FetchLibrarians(self):
        self.cursor.execute("""
            SELECT C.firstName, C.lastName, C.email
            FROM Customer C
            JOIN Librarian L ON L.customerID = C.customerID""")
        librarians = self.cursor.fetchall()
        print("Here is a current list of librarians you can contact:")
        for lib in librarians:
            print(lib[0] + " " + lib[1] + ": " + lib[2])