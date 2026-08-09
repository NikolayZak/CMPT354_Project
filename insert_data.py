import sqlite3

# open the database
DB_FILE = "library.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

with open("schema.sql", "r") as file:
    schema = file.read()

cursor.executescript(schema)


# data
customers = [
    ("Bob", "Smith", "Bob@gmail.com"),
    ("Fred", "Anderson", "Fred@hotmail.com"),
    ("Billy", "Johnson", "Billy@gmail.com")
]

items = [
    ("The Hobbit", "Book"),
    ("1984", "Book"),
    ("Dune", "Book"),
    ("Inception", "DVD")
]

# insert data
cursor.executemany("""
    INSERT INTO Customer (firstName, lastName, email)
    VALUES (?, ?, ?)
""", customers)

cursor.executemany("""
    INSERT INTO Item (name, type)
    VALUES (?, ?)
""", items)

conn.commit()
conn.close()

print("Database populated successfully.")