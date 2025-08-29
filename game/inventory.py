# Player ke paas jo items rahenge unke liye inventory system
# Yeh inventory simple list based hai (Hinglish comment)


class Inventory:
    def __init__(self):
        # items list store karega saare gathered items
        self.items = []

    def add_item(self, item):
        # Agar pehle se nahi hai to add karo
        if item not in self.items:
            self.items.append(item)

    def has_item(self, item):
        # Check karo inventory mein item hai ya nahi
        return item in self.items


player_inventory = Inventory()