# Player ke paas jo items rahenge unke liye inventory system

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)

    def has_item(self, item):
        return item in self.items

player_inventory = Inventory()