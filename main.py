from methods.db_api import Database
import methods.interface as interface

db = Database()

print("Welcome to the library Database")
while(True):
    user_selection = interface.GetInput()

    match user_selection:
        case 0: # Find Item
            item_name = input("Item name (if known): ")
            item_type = input("Item type (if known): ")
            information = db.FindItem(item_name, item_type)
            print(information)
            continue
        case 1: # Borrow Item
            continue
        case 2: # Return Item
            continue
        case 3: # Donate Item
            continue
        case 4: # Find Event
            continue
        case 5: # Register for an Event
            continue
        case 6: # Volunteer
            continue
        case 7: # Ask For Help
            continue
        case 8: # exit
            break

db.Close()