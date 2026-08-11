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
            customer_id = input("customer ID: ")
            item_id = input("item_id: ")
            db.BorrowItem(customer_id, item_id)
            continue
        case 2: # Return Item
            item_id = input("item_id: ")
            db.ReturnItem(item_id)
            continue
        case 3: # Donate Item
            item_name = input("Item name: ")
            item_type = input("Item type: ")
            db.DonateItem(item_name, item_type)
            continue
        case 4: # Find Event
            event_name = input("Event name (if known): ")
            information = db.FindEvent(event_name)
            print(information)
            continue
        case 5: # Register for an Event
            customer_id = input("Customer ID: ")
            event_id = input("Event ID: ")
            db.RegisterForEvent(customer_id, event_id)
            continue
        case 6: # Volunteer
            customer_id = input("Customer ID: ")
            time = input("Volunteer time: ")
            date = input("Volunteer date: ")
            db.Volunteer(customer_id, time, date)
            continue
        case 7: # Ask For Help
            db.FetchLibrarians()
            continue
        case 8: # exit
            break

db.Close()