import sqlite3

# open the database
DB_FILE = "library.db"

conn = sqlite3.connect(DB_FILE)
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

with open("schema.sql", "r") as file:
    schema = file.read()

cursor.executescript(schema)


# data
customers = [
    ("Bob", "Smith", "Bob@gmail.com"),
    ("Fred", "Anderson", "Fred@hotmail.com"),
    ("Billy", "Johnson", "Billy@gmail.com"),
    ("Alice", "Chen", "alice.chen@gmail.com"),
    ("Maria", "Garcia", "maria.garcia@gmail.com"),
    ("Liam", "Brown", "liam.brown@gmail.com"),
    ("Priya", "Patel", "priya.patel@gmail.com"),
    ("Noah", "Wilson", "noah.wilson@gmail.com"),
    ("Emma", "Davis", "emma.davis@gmail.com"),
    ("Omar", "Hassan", "omar.hassan@gmail.com"),
    ("Grace", "Kim", "grace.kim@library.ca"),
    ("Daniel", "Wong", "daniel.wong@library.ca"),
    ("Olivia", "Martin", "olivia.martin@library.ca"),
    ("Ethan", "Clark", "ethan.clark@library.ca"),
    ("Ava", "Thompson", "ava.thompson@library.ca"),
    ("Lucas", "Moore", "lucas.moore@library.ca"),
    ("Mia", "Taylor", "mia.taylor@library.ca"),
    ("Henry", "White", "henry.white@library.ca"),
    ("Chloe", "Lewis", "chloe.lewis@library.ca"),
    ("Jack", "Walker", "jack.walker@library.ca")
]

items = [
    ("The Hobbit", "Book"),
    ("1984", "Book"),
    ("Dune", "Book"),
    ("Inception", "DVD"),
    ("Pride and Prejudice", "Book"),
    ("Clean Code", "Book"),
    ("Spirited Away", "DVD"),
    ("Interstellar", "DVD"),
    ("National Geographic", "Magazine"),
    ("Catan", "Board Game")
]

future_additions = [
    ("Project Hail Mary", "Book", 8),
    ("The Bear", "DVD", 5),
    ("Wingspan", "Board Game", 7),
    ("Scientific American", "Magazine", 4),
    ("Tomorrow, and Tomorrow, and Tomorrow", "Book", 6),
    ("Oppenheimer", "DVD", 9),
    ("Azul", "Board Game", 3),
    ("The New Yorker", "Magazine", 5),
    ("The Three-Body Problem", "Book", 10),
    ("Past Lives", "DVD", 4)
]

rooms = [
    ("Main Hall", 100),
    ("Meeting Room A", 20),
    ("Meeting Room B", 20),
    ("Study Room 1", 6),
    ("Study Room 2", 6),
    ("Computer Lab", 30),
    ("Children's Room", 25),
    ("Community Room", 50),
    ("Quiet Room", 12),
    ("Media Room", 15)
]

events = [
    ("Summer Reading Club", "Reading", "Weekly reading club for all ages."),
    ("Python Basics", "Workshop", "Introduction to Python programming."),
    ("Family Movie Night", "Movie", "A family-friendly evening movie."),
    ("Resume Writing", "Workshop", "Help creating and improving resumes."),
    ("Children's Story Time", "Reading", "Stories and activities for children."),
    ("Local History Talk", "Lecture", "A talk about local community history."),
    ("Board Game Afternoon", "Social", "Play library board games with others."),
    ("English Conversation Circle", "Language", "Practice conversational English."),
    ("Digital Privacy", "Workshop", "Learn how to stay safer online."),
    ("Book Donation Drive", "Community", "Community collection of donated books.")
]

records = [
    (1, 1, "2026-06-01 10:00:00", "2026-06-14 11:30:00"),
    (2, 2, "2026-06-05 13:00:00", "2026-06-18 09:15:00"),
    (3, 3, "2026-06-12 15:30:00", "2026-06-25 16:00:00"),
    (4, 4, "2026-07-01 12:00:00", "2026-07-10 14:20:00"),
    (5, 5, "2026-07-08 09:00:00", "2026-07-20 10:00:00"),
    (6, 6, "2026-08-01 10:00:00", None),
    (7, 7, "2026-08-02 11:00:00", None),
    (8, 8, "2026-08-03 12:00:00", None),
    (9, 9, "2026-08-04 13:00:00", None),
    (10, 10, "2026-08-05 14:00:00", None)
]

bookings = [
    (1, "Main Hall", "2026-08-15 10:00:00", "2026-08-15 12:00:00"),
    (2, "Computer Lab", "2026-08-16 13:00:00", "2026-08-16 15:00:00"),
    (3, "Media Room", "2026-08-17 18:00:00", "2026-08-17 20:00:00"),
    (4, "Meeting Room A", "2026-08-18 10:00:00", "2026-08-18 12:00:00"),
    (5, "Children's Room", "2026-08-19 09:00:00", "2026-08-19 10:30:00"),
    (6, "Community Room", "2026-08-20 14:00:00", "2026-08-20 16:00:00"),
    (7, "Meeting Room B", "2026-08-21 13:00:00", "2026-08-21 16:00:00"),
    (8, "Study Room 1", "2026-08-22 11:00:00", "2026-08-22 12:30:00"),
    (9, "Quiet Room", "2026-08-23 15:00:00", "2026-08-23 17:00:00"),
    (10, "Study Room 2", "2026-08-24 10:00:00", "2026-08-24 12:00:00")
]

librarians = [(customer_id,) for customer_id in range(11, 21)]

volunteers = [
    (1, "09:00:00", "2026-08-15"),
    (2, "10:00:00", "2026-08-16"),
    (3, "11:00:00", "2026-08-17"),
    (4, "12:00:00", "2026-08-18"),
    (5, "13:00:00", "2026-08-19"),
    (6, "14:00:00", "2026-08-20"),
    (7, "15:00:00", "2026-08-21"),
    (8, "16:00:00", "2026-08-22"),
    (9, "17:00:00", "2026-08-23"),
    (10, "18:00:00", "2026-08-24")
]

event_guests = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10)
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

cursor.executemany("""
    INSERT INTO FutureAddition (name, type, demand)
    VALUES (?, ?, ?)
""", future_additions)

cursor.executemany("""
    INSERT INTO Room (location, capacity)
    VALUES (?, ?)
""", rooms)

cursor.executemany("""
    INSERT INTO Event (name, type, description)
    VALUES (?, ?, ?)
""", events)

cursor.executemany("""
    INSERT INTO Record (customerID, itemID, checkoutDate, returnDate)
    VALUES (?, ?, ?, ?)
""", records)

cursor.executemany("""
    INSERT INTO Booking (eventID, location, startTime, endTime)
    VALUES (?, ?, ?, ?)
""", bookings)

cursor.executemany("""
    INSERT INTO Librarian (customerID)
    VALUES (?)
""", librarians)

cursor.executemany("""
    INSERT INTO Volunteer (customerID, Vtime, Vdate)
    VALUES (?, ?, ?)
""", volunteers)

cursor.executemany("""
    INSERT INTO EventGuest (customerID, eventID)
    VALUES (?, ?)
""", event_guests)

conn.commit()
conn.close()

print("Database populated successfully.")