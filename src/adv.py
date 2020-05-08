from player import Player
from dicts import room
from dicts import items

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
    print()
    print("*" * 50)
    print("*" * 40)
    print("*" * 30)
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
            "\nDo you want to pick up an item? \n\nif yes input the number next to the item,\nif no hit enter --> \t"
        )

    if not itemChoice == "" and adventurer.currentRoom.item_list[int(itemChoice)]:
        selectedItem = int(itemChoice)
        adventurer.getItem(adventurer.currentRoom.item_list[selectedItem])
        print(
            "\nYou juct picked up a %s"
            % (adventurer.currentRoom.item_list[selectedItem].name)
        )

    dropItemChoice = input(
        "\nBefore you move on would you like to drop an item? \n\nif yes input the number next to the item in your inventory,\nif no hit enter --> \t"
    )

    if not dropItemChoice == "" and adventurer.items[int(dropItemChoice)]:
        selectedItem = int(dropItemChoice)
        adventurer.dropItem(adventurer.items[selectedItem])
        print("\nYou just droped a %s" % (adventurer.items[selectedItem].name))

    choice = input(
        "\nSelect the direction in which to proceed [n, s, e, w]\nor press [q] to exit --> \t"
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
