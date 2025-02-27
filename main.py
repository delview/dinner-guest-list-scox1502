main_guest = []
amount_of_no = 0 
amount_of_guests = 6
import random

while True:
    if amount_of_guests == 6:
        guest1 = input("who would you like to invite first? ")
    amount_of_guests -= 1
    main_guest.append(guest1)
    choice = input(f"you want {guest1} to be at your party? [y/n] ")
    print(f"you can have {amount_of_guests} more people at the party")

    if choice == "y":
        break
        
    elif choice == "n":
        amount_of_guests += 1
        pass

    else:
        print("that is not an option try again")
        pass

    if amount_of_guests == 5:
        guest2 = input("who would you like to invite second? ")
    main_guest.append(guest2)
    amount_of_guests -= 1
    choice = input(f"you want {guest2} to be at your party? [y/n] ")
    print(f"you can have {amount_of_guests} more people at the party")
    if choice == "y":
        break
        
    elif choice == "n":
        amount_of_guests += 1
        pass

    else:
        print("that is not an option try again")
        pass

    if amount_of_guests == 4:
        guest3 = input("who would you like to invite third? ")
    main_guest.append(guest3)
    amount_of_guests -= 1
    choice = input(f"you want {guest3} to be at your party? [y/n] ")
    print(f"you can have {amount_of_guests} more people at the party")
    if choice == "y":
        break
        
    elif choice == "n":
        amount_of_guests += 1
        pass

    else:
        print("that is not an option try again")
        pass


    if amount_of_guests == 3:
        guest4 = input("who would you like to invite forth? ")
    main_guest.append(guest4)
    amount_of_guests -= 1
    choice = input(f"you want {guest4} to be at your party? [y/n] ")
    print(f"you can have {amount_of_guests} more people at the party")
    if choice == "y":
        break
        
    elif choice == "n":
        amount_of_guests += 1
        pass

    else:
        print("that is not an option try again")
        pass

    if amount_of_guests == 2:
        guest5 = input("who would you like to invite fifth? ")
    main_guest.append(guest5)
    amount_of_guests -= 1
    choice = input(f"you want {guest5} to be at your party? [y/n] ")
    print(f"you can have {amount_of_guests} more people at the party")
    if choice == "y":
        break
        
    elif choice == "n":
        amount_of_guests += 1
        pass

    else:
        print("that is not an option try again")
        pass

    if amount_of_guests == 1:
        guest6 = input("who would you like to invite sixth? ")
    main_guest.append(guest6)
    amount_of_guests -= 1
    choice = input(f"you want {guest6} to be at your party? [y/n] ")
    if choice == "y":
        break
        
    elif choice == "n":
        amount_of_guests += 1
        pass

    else:
        print("that is not an option try again")
        pass

    print(f"you can have {amount_of_guests} more people at the party")
    


    if amount_of_guests == 0:
        print("you have invited everyone")
        break
    

while True:

    random_number = random.randint(main_guest)
