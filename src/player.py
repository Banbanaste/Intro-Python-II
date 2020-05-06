# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, currentRoom=None):
        self.currentRoom = currentRoom
    
    def setCurrentRoom(self, choice):
        if hasattr(self.currentRoom, choice):
            newRoom = getattr(self.currentRoom, choice)
            self.currentRoom = newRoom
        else:
            print("\nYou can't go in that direction, try again!\n")
        
