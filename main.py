import random

main_guest = []
main_invites = []
amount_of_guests = 6
new_guest = []

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
        
print("ok lets make an invitation letter for everyone :)")
print(f"lets make a letter for {main_guest[0]} first")
invites = input(f"dear {main_guest [0]} ")
main_invites.append(invites)
print(f"the second invite letter will be for {main_guest [1]}")
invites = input(f"dear {main_guest [1]} ")
main_invites.append(invites)
print(f"time for {main_guest [2]} invitation")
invites = input(f" dear {main_guest [2]} ")
main_invites.append(invites)
print(f"its {main_guest [3]} time for an invite")
invites = input(f"dear {main_guest [3]} ")
main_invites.append(invites)
print(f"we cant leave {main_guest [4]} out")
invites = input(f"dear {main_guest [4]} ")
main_invites.append(invites)
print(f"cant forget {main_guest [5]}")
invites = input(f"dear {main_guest [5]} ")
main_invites.append(invites)
print(f"and {main_guest [6]} was saved best for last")
main_invites.append(invites)

random_index = random.randint(0, len(main_guest) - 1)
random_person = main_guest[random_index]
print(f"oh no {random_person} was unable to come")
print("we need to invite someone new")
new_guest = input("lets replace {random_person} with ")

random_person = new_guest

print(main_guest)