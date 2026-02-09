def main():
    display_menu()

def display_menu():
    user_name = input("user full name:")
    print("-main menu-")
    print("1. view members")
    print("2. Add member")
    print("3. Remove member")
    print("4. Update rank")
    print("5. Search member")
    print("6.filter by division")
    print("7. Calcualte payroll")
    print("8. Count officers")
    print("9. Analyze Data")
    print("10. Exit")
    opt = input("Select option: ")
    yes = print("bfuai")
    options = {
        1: init_database(),
        2: add_member('database'),
        3:yes,
        4:yes,
        5:yes,
        6:yes,
        7:yes,
        8:yes,
        9:yes,
        10:yes,
        }



def init_database():
    database = [
        {"n":"Picard", "r":"Captain", "d":"Command", "id":"023"},
        {"n":"Riker", "r":"Commander", "d":"Command", "id":"024"},
        {"n":"Data", "r":"Lt. Commander", "d":"Operations", "id":"025"},
        {"n":"Worf", "r":"Lieutenant", "d":"Security", "id":"026"},
    ]
    for entry in database:
        # Unpacks all values in the dictionary and joins them with a comma
        print(*entry.values(), sep=", ")
    
    return database
def add_member(database):
    name = input("Enter Name: ")
    rank = input("Enter Rank: ")
    dept = input("Enter Department: ")
    id_num = input("Enter ID: ")
    
    # Create the dictionary and add it
    new_entry = {"n": name, "r": rank, "d": dept, "id": id_num}
    database.append(new_entry)
    print(f"Successfully added {name} to the database.")





main()


