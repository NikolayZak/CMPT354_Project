MenuItem = [
    "Find Item",   # 0
    "Borrow Item", # 1
    "Return Item", # 2
    "Donate Item", # 3
    "Create Event",# 4
    "Find Event",  # 5
    "Volunteer",   # 6
    "Ask For Help",# 7
    "Exit"         # 8
]


def PrintMenu():
    for i in range(len(MenuItem)):
        print(str(i) + ") " + MenuItem[i])

def GetInput():
    while True:
        PrintMenu()
        text = ""
        try:
            text = input("Please select an option: ")
            choice = int(text)

            if 0 <= choice < len(MenuItem):
                return choice

            print(f"Error: {choice} is out of range (0-{len(MenuItem) - 1})")
        except ValueError:
            print(f"Error: {text} is not a number between (0-{len(MenuItem) - 1})")
