from db_api import Database
import interface

db = Database()

print("Welcome to the library Database")
while(True):
    input = interface.GetInput()

    match input:
        case 0: # Find Item
            continue
        case 1: # Borrow Item
            continue
        case 2: # Return Item
            continue
        case 3: # Donate Item
            continue
        case 4: # Create Event
            continue
        case 5: # Find Event
            continue
        case 6: # Volunteer
            continue
        case 7: # Ask For Help
            continue
        case 8: # exit
            break

db.Close()