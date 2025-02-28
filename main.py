main_guest = []
amount_of_guests = 6

while amount_of_guests > 0:
    guest = input("Who would you like to invite? ")
    choice = input(f"Do you want {guest} to be at your party? [y/n] ")

    if choice.lower() == "y":
        main_guest.append(guest)
        amount_of_guests -= 1
        print(f"You can have {amount_of_guests} more people at the party.")
    elif choice.lower() == "n":
        print("Alright, let's invite someone else.")
    else:
        print("That is not an option. Try again.")
        
print("You have invited everyone:")

