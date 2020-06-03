# the game items
# import player from Player

class Item():
    def __init__(self, name, description): # Would be fun to add the price of an item or a shop to purchase upgrades.
        self.name = name
        self.description = description

    def pick_up(self):
        print(f"{self.name} was picked up!")

    def drop(self):
        print(f"{self.name} was dropped")
