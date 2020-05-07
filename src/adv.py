from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}

items = {
    "outside": [
        ("lamp", "brightens the place up, smells like alcohol"),
        ("rag", "could be used to clean sweat from your brow"),
    ],
    "foyer": [
        ("map", "directions seem inconsistant with this adventure, but who knows")
    ],
    "overlook": [
        ("twig", "can be used for poking"),
        ("pouch", "maybe this had some money in it once"),
    ],
    "narrow": [("candy bar", "ooh a piece of candy")],
}

# Link rooms together
room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

# Add Items to rooms
room["outside"].item_list = [
    Item(itemSet[0], itemSet[1], items["outside"].index(itemSet))
    for itemSet in items["outside"]
]
room["foyer"].item_list = [
    Item(itemSet[0], itemSet[1], items["foyer"].index(itemSet))
    for itemSet in items["foyer"]
]
room["overlook"].item_list = [
    Item(itemSet[0], itemSet[1], items["overlook"].index(itemSet))
    for itemSet in items["overlook"]
]
room["narrow"].item_list = [
    Item(itemSet[0], itemSet[1], items["narrow"].index(itemSet))
    for itemSet in items["narrow"]
]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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
adventurer = Player(room["outside"])
directions = ["n", "s", "e", "w"]

while True:
    print("*" * 50)
    print("\nYou are in the:\t%s" % (adventurer.currentRoom.name))
    print(adventurer.currentRoom.description)
    if len(adventurer.items) > 0:
        print("\nyou are currently carrying:")
        for i in adventurer.items:
            print(i)

        print("_" * 50 + "/")

    if len(adventurer.currentRoom.item_list) > 0:
        print("\nBefore you go, there seem to be some items here:")
        for itemSet in adventurer.currentRoom.item_list:
            print(itemSet)

        itemChoice = input(
            "\nDo you want to pick up an item? \n\nif yes input the number next to the item,\nif no hit enter\n"
        )

    if not itemChoice == "" and adventurer.currentRoom.item_list[int(itemChoice)]:
        selectedItem = int(itemChoice)
        adventurer.getItem(adventurer.currentRoom.item_list[selectedItem])
        print(
            "\nYou juct picked up a %s"
            % (adventurer.currentRoom.item_list[selectedItem].name)
        )

    dropItemChoice = input(
        "\nBefore you move on would you like to drop an item? \n\nif yes input the number next to the item in your inventory,\nif no hit enter\n"
    )

    if not dropItemChoice == "" and adventurer.items[int(dropItemChoice)]:
        selectedItem = int(dropItemChoice)
        adventurer.dropItem(adventurer.items[selectedItem])
        print("\nYou just droped a %s" % (adventurer.items[selectedItem].name))

    choice = input(
        "\nSelect the direction in which to proceed [n, s, e, w]\nor press [q] to exit:\n"
    )

    if choice == "q":
        print("\nYour next adventure awaits!\n")
        break

    try:
        if directions.count(choice) > 0:
            choiceName = choice + "_to"
            adventurer.setCurrentRoom(choiceName)
        else:
            print("\noops! Please select a cardinal direction [n, s, e, w]\n")
    except ValueError:
        print("there was an error, exiting the script now")
        break
