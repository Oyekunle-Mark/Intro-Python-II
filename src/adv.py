import textwrap
from room import Room
from player import Player
from item import Item
import formatting

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


room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


formatting.headline('Welcome to the Treasure Hunt Adventure Game')

formatting.details(
    "Use keys n, s, e and w to move the player North, South, East and West.")
formatting.details("Get items with get/take [item]")
formatting.details("Drop items with drop [item]")
formatting.details("Use i or inventory to view your inventory.")

player = Player("Player", room['outside'])


def print_room(room):
    formatting.message(f"Current room: {room.name}")
    formatting.message(textwrap.fill(room.description, width=50))

    formatting.message("Items in room:")

    if len(room.items) > 0:
        for item in room.items:
            formatting.message(f"  - {item}")
    else:
        formatting.message("    This room is empty.")


def move_player(direction, player):
    dir = f"{direction}_to"

    if getattr(player.current_room, dir) == None:
        formatting.error(
            "There is no room in that direction adventurer!")
    else:
        player.current_room = getattr(player.current_room, dir)


print_room(player.current_room)

while True:
    print()
    user_input = input("[n/s/e/w]: ").lower().split()

    if len(user_input) == 1:
        user_input = user_input[0]

        # if user_input == 'n':
        #     if player.current_room.n_to == None:
        #         formatting.error(
        #             "There is no room in that direction adventurer!")
        #         continue

        #     player.current_room = player.current_room.n_to

        # elif user_input == 's':
        #     if player.current_room.s_to == None:
        #         formatting.error(
        #             "There is no room in that direction adventurer!")
        #         continue

        #     player.current_room = player.current_room.s_to

        # elif user_input == 'e':
        #     if player.current_room.e_to == None:
        #         formatting.error(
        #             "There is no room in that direction adventurer!")
        #         continue

        #     player.current_room = player.current_room.e_to

        # elif user_input == 'w':
        #     if player.current_room.w_to == None:
        #         formatting.error(
        #             "There is no room in that direction adventurer!")
        #         continue

        #     player.current_room = player.current_room.w_to

        if user_input in ['n', 's', 'e', 'w']:
            move_player(user_input, player)
        elif user_input == 'i' or user_input == 'inventory':
            player.show_inventory()
            continue
        elif user_input == 'q':
            formatting.details("Thanks for playing.")
            break
        else:
            formatting.error("Invalid input!")
            continue

    elif len(user_input) == 2:
        command, item = user_input

        if command == 'get' or command == 'take':
            if player.current_room.item_exist(item):
                removed_item = player.current_room.remove_item(item)
                removed_item.on_take()
                player.add_item(removed_item)
            else:
                formatting.error(f"Room does not contain {item}")
                continue

        elif command == 'drop':
            if player.item_exist(item):
                removed_item = player.remove_item(item)
                removed_item.on_drop()
                player.current_room.add_item(removed_item)
            else:
                formatting.error(f"Your inventory does not contain {item}")
                continue

        else:
            formatting.error("Invalid input!")
            continue

    else:
        formatting.error("Invalid input!")
        continue

    print_room(player.current_room)
