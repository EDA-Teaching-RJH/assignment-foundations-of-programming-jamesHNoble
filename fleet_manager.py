def main():
    names, ranks, division, ids = init_database()
    user_name = input("user full name:")
    print(user_name, " logged in!")
    option_choice(names, ranks, division, ids)

def option_choice(names, ranks, division, ids):
    while True:
        opt = display_menu()

        if opt == "1":
            display_data(names, ranks, division, ids)
        elif opt == "2":
            add_member(names, ranks, division, ids)
        elif opt == "3":
            remove_member(names, ranks, division, ids)
        elif opt == "4":
            rank_updater(names, ranks, division, ids)
        elif opt == "5":
            search_member(names, ranks, division, ids)
        elif opt == "6":
            division_filter(names, division)
            print("Loading........................")
            option_choice(names, ranks, division, ids)
        elif opt == "7":
            payroll = payroll_calculation(ranks)
            print("current cost of members: ", payroll)
            print("Loading........................")
            option_choice(names, ranks, division, ids)
        elif opt == "8":
            count = Jedi_count(ranks)
            print("Number of Jedi: ", count)
            print("Loading........................")
            option_choice(names, ranks, division, ids)
        elif opt == "9":
            print("Exiting...")
        break


def display_menu():
    print("\n--- MENU ---")
    print("1: View Crew Members")
    print("2: Add Crew Member")
    print("3: Remove Crew Member")
    print("4: Update Rank")
    print("5: Search Crew Name")
    print("6: Filter By Division")
    print("7: Calculate Payroll")
    print("8: Count Jedi")
    print("9: Quit")

    op = input("Select option: ")

    return op
        

def display_data(n, r, d, i):
    print(f"{'ID':<5} {'Name':<10} {'Rank':>20} {'Division':>20}")
    print("---------------------------------------------------------------------------")

    for id, name, rank, division in zip(i, n, r, d):
        print(f"{id:<5} {name:<10} {rank:>20} {division:>20}")
    print("Loading........................")
    option_choice(n, r, d, i)


def init_database():
    n = ["Luke", "Obiwan", "Han solo", "Jarjar", "Rex"]
    r = ["Jedi", "Jedi", "Rebel", "Senetor", "commander"]
    d = ["Rebel", "Republic", "Rebel", "Gungan", "Trooper"]
    i = ["1", "2", "3", "4", "5"]
    return n, r, d, i


def add_member(n, r, d, i):
    name = input("enter new name: ")
    n.append(name)
    rank = input("enter the rank: ")
    r.append(rank)
    division = input("enter the division: ")
    d.append(division)
    id = input("enter the id of the person: ")
    i.append(id)
    print("Loading........................")
    option_choice(n, r, d, i)
    return n, r, d, i

def remove_member(n, r, d, i):
    num = input("Please enter the Id you with to remove: ")

    index = i.index(num)
    n.pop(index)
    r.pop(index)
    d.pop(index)
    i.pop(index)
    print("Loading........................")
    option_choice(n, r, d, i)
    return n, r, d, i

def rank_updater(n, r, d, i):
    num = input("PLease enter the Id of the member you wish to update:")
    up_rank = input("Please enter the new rank of this member: ")

    for int in range(len(i)):
        if i[int] == num:
            r[int] = up_rank
    print("Loading........................")
    option_choice(n, r, d, i)

def search_member(n, r, d, i):
    num = input("Please enter the Id of the member you wish to search: ")
    print(f"{'ID':<5} {'Name':<5} {'Rank':>5} {'Division':>5}")
    print("---------------------------------------------------------------------------")
    for int in range(len(n)):
        if num == i[int]:
            print(i[int], " ", n[int], " ", r[int], " ", d[int])
    print("Loading........................")
    option_choice(n, r, d, i)

def division_filter(n, d):
    opt = input("Please input a division[Rebel, Republic, Gungan, Trooper]: ")
    
    if opt == "Rebel" or opt == "Republic" or opt == "Gungan" or opt == "Trooper":
        for I in range(len(n)):
            if d[I] == "Rebel" and opt == "Rebel":
                print(n[I], " ", d[I])
            elif d[I] == "Republic" and opt == "Republic":
                print(n[I], " ", d[I])

            elif d[I] == "Gungan" and opt == "Gungan":
                print(n[I], " ", d[I])

            elif d[I] == "Trooper" and opt == "Trooper":
                print(n[I], " ", d[I])
    else:
        print("Invalid")
    

def payroll_calculation(ranks):
    payroll = 0
    for i in range(len(ranks)):
        if ranks[i] == "Rebel":
            payroll += 100
        elif ranks[i] == "Commander":
            payroll += 200
        elif ranks[i] == "jedi":
            payroll += 500
        elif ranks[i] == "Senetor":
            payroll += 1000
    return(payroll)


def Jedi_count(ranks):
    count = 0
    for i in range(len(ranks)):
        if ranks[i] == "Jedi":
            count = count + 1

    return count

main()