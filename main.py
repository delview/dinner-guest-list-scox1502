#goal: make a way to invite some people to a party and make sure you are able to replace people.
import random

main_guest = []
main_invites = []
new_guest = []
#ask how many people you want to invite
while True:
    amount_of_guests = input("How many people would you like to invite to the party? ")
    if amount_of_guests.isdigit():
        amount_of_guests = int(amount_of_guests)
        choice = input(f"You want {amount_of_guests} people to come to the party? [y/n] ")
        if choice.lower() == "y":
            print("Ok")
            break
        elif choice.lower() == "n":
            print("Ok then")
    else:
        print("The input is not a valid number. Please enter a valid number.")

# Ask who you want to invite
while amount_of_guests > 0:
    guest = input("Who would you like to invite? ")
    choice = input(f"Do you want {guest} to be at your party? [y/n] ")
    if choice.lower() == "y":
        main_guest.append(guest)
        amount_of_guests -= 1
        if amount_of_guests > 0:
            print(f"You can invite {amount_of_guests} more people to the party.")
        else:
            print("Your guest list is full.")
    elif choice.lower() == "n":
        print("Alright, let's invite someone else.")
    else:
        print("That is not an option. Try again.")


#make a letter for everyone you invited
# Make invitation letters for everyone you invited
print("Ok, let's make invitation letters for everyone!")

for invite, guest in enumerate(main_guest):
    if invite == 0:
        print(f"Ok, let's start with {guest}.")
    elif invite == len(main_guest) - 1:
        print(f"Ok, and {guest} last.")
    else:
        print(f"Next, let's do {guest}.")
    
    invite = input(f"Dear {guest}, ")
    main_invites.append(invite)

#make it so that you can replace someone you invited

choice = input("Would you like to replace anyone? [y/n] ").lower()
while choice == "y":
    print("People you have invited:")
    for guest in main_guest:
        print(guest)
    
    replace_person = input("Who would you like to replace? ")
    if replace_person in main_guest:
        new_person = input("And who would you like to replace them with? ")
        index = main_guest.index(replace_person)
        main_guest[index] = new_person
        print(f"{replace_person} has been replaced with {new_person}.")
    else:
        print(f"{replace_person} is not on the guest list.")
    
    choice = input("Would you like to replace anyone else? [y/n] ")
#show who has been invited
for main_guest in main_guest:
    print(f" you have invited:{main_guest}")