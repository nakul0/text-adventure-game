# Player ke paas jo items rahenge unke liye inventory system

class Inventory:
    def __init__(self):
        self.items = []   # Empty inventory list

    def add_item(self, item):
        self.items.append(item)
        print(f"👜 {item} inventory me add ho gaya!")

    def show_inventory(self):
        if not self.items:
            print("Inventory khali hai.")
        else:
            print("Tumhari Inventory:")
            for item in self.items:
                print(f"- {item}")
