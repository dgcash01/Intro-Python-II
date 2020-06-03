from room import Room
from hero import Hero
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

items = {
    "sword": Item("Sword", "Stick them with the pointy end."),
    "lantern": Item("Lantern", "This will be helpful in the dark."),
    "shovel": Item("Shovel", "This could be used to bludgen or dig.")

    # Possible new items

    # "axe": Item("Axe", "This could be used to chop wood or heads.")
    # "long sword": Item("Long Sword", "This is used to stab things better."),
    # "shield": Item("Shield", "This could be used to defend yourself and add armor")
}

room['outside'].items.append(items["lantern"])
room['overlook'].items.append(items["sword"])
room['narrow'].items.append(items["shovel"])

# add more locations and possibly more items to game

# Make a new hero object that is currently in the 'outside' room.

new_hero = Hero(hero_name = "Dan", current_room = room["outside"])
print ("\nWelcome Hero! You may enter a direction in which to travel with n, s, e, w.  You may also use q to quit the game.\n\nYou may also type get, take, pickup as your actions")
print(f"{new_hero.hero_name} is {new_hero.current_room} \n")
print(new_hero.current_room.list_items())

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    
    selection = input("Enter a direction, command or Q to escape: ")
    user_selection = selection.lower().split(" ")
    if len(user_selection) == 1: 
        if selection == "q": 
            print("Have a good day. Thanks for playing.")
            break
        elif selection == "n" or selection == "s" or selection == "e" or selection == "w":
            new_hero.move_room(selection)
            print(f"\n{new_hero.hero_name} is {new_hero.current_room.room_name} \n{new_hero.current_room.description}\n\n {new_hero.current_room.list_items()}")
        elif selection == "i":
            new_hero.print_items()
        else:
            print("That is not a proper command.")
            # Need to add logic for misspelling item names
    elif len(user_selection) == 2: 
        if user_selection[0] in ["take", "get", "pickup"]:
            if items[user_selection[2]]:
                new_hero.pickup_item(items[user_selection[1]])
                print("\n\nYou have added a new item to inventory!\n")
                print(new_hero.print_items())
                print(f"{new_hero.hero_name} is {new_hero.current_room} \n")
                print(new_hero.current_room.list_items())
            else:
                print("That isn't an item.")
        elif user_selection[0] == "drop": 
            if items[user_selection[1]]:
                new_hero.drop_item(items[user_selection[1]])
                print("You dropped an item!")
                print(new_hero.print_items())
                print(f"{new_hero.hero_name} is {new_hero.current_room} \n")
                print(new_hero.current_room.list_items())
            else: 
                print("That isn't an item.")
        else: 
            print("That is not a proper command.")
    else: 
        print("That is not a proper command.")

# If the user enters a cardinal direction, attempt to move to the room there.

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
