class Item:
    def __init__(self, name, description, place):
        self.place = place
        self.name = name
        self.description = description

    def __str__(self):
        return "\n[%d]\tname: %s\n\tdescription: %s" % (
            self.place,
            self.name,
            self.description,
        )
