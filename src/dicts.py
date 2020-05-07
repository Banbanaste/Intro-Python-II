from room import Room
from item import Item

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
