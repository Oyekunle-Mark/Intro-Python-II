import textwrap
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item("Lantern"), Item("Axe"), Item("Bellow")]),

    'foyer':    Room("Foyer",
                     """Dim light filters in from the south. Dusty
passages run north and east.""",
                     [Item("Coal"), Item("Needle"), Item("Gun")]),

    'overlook': Room("Grand Overlook",
                     """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [Item("Pellet"), Item("Plates"), Item("Book")]),

    'narrow':   Room("Narrow Passage",
                     """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     [Item("Shovel"), Item("Barrow"), Item("Anvil")]),

    'treasure': Room("Treasure Chamber",
                     """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [Item("Chest"), Item("Bag"), Item("Spear")]),
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

print("\n\nWelcome to the Treasure Hunt Adventure Game. \n")
print("Use keys n, s, e and w to move the player North, South, East and West.")
print("Get items with get/take [item]")
print("Drop items with drop [item]")
print("Use i or inventory to view your inventory.\n")

# Make a new player object that is currently in the 'outside' room.

player = Player("Player", room['outside'])


def print_room(room):
    print("\nCurrent room: ", room.name)
    print(textwrap.fill(room.description, width=50), '\n')

    print("Items in room:")

    if len(room.items) > 0:
        for item in room.items:
            print("  - ", item)
    else:
        print("    This room is empty.")

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
    print_room(player.current_room)

    user_input = input("[n/s/e/w]: ").split()

    if len(user_input) == 1:
        user_input = user_input[0]

        if user_input == 'n':
            if player.current_room.n_to == None:
                print("\nThere is no room in that direction adventurer!")
                continue

            player.current_room = player.current_room.n_to

        elif user_input == 's':
            if player.current_room.s_to == None:
                print("\nThere is no room in that direction adventurer!")
                continue

            player.current_room = player.current_room.s_to

        elif user_input == 'e':
            if player.current_room.e_to == None:
                print("\nThere is no room in that direction adventurer!")
                continue

            player.current_room = player.current_room.e_to

        elif user_input == 'w':
            if player.current_room.w_to == None:
                print("\nThere is no room in that direction adventurer!")
                continue

            player.current_room = player.current_room.w_to

        elif user_input == 'i' or user_input == 'inventory':
            player.show_inventory()

        elif user_input == 'q':
            print("Thanks for playing.")
            break

    elif len(user_input) == 2:
        command, item = user_input

        if command == 'get' or command == 'take':
            if player.current_room.item_exist(item):
                removed_item = player.current_room.remove_item(item)
                removed_item.on_take()
                player.add_item(removed_item)
            else:
                print(f"Room does not contain {item}")

        elif command == 'drop':
            if player.item_exist(item):
                removed_item = player.remove_item(item)
                removed_item.on_drop()
                player.current_room.add_item(removed_item)
            else:
                print(f"Your inventory does not contain {item}")
