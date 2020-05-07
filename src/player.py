# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, currentRoom=None):
        self.currentRoom = currentRoom
        self.items = []

    def setCurrentRoom(self, choice):
        if hasattr(self.currentRoom, choice):
            newRoom = getattr(self.currentRoom, choice)
            self.currentRoom = newRoom
        else:
            print("\nYou can't go in that direction, try again!\n")

    def getItem(self, item):
        if not item in self.items:
            self.items.append(item)
            newLocation = self.items.index(item)
            item.place = newLocation

    def dropItem(self, item):
        toDelete = self.items.index(item)
        if toDelete:
            self.currentRoom.itemList.append(item)
            newLocation = self.currentRoom.itemList.index(item)
            elf.currentRoom.itemList[-1].place = newLocation
            del self.items[toDelete]
