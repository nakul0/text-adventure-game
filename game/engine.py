# Engine file: yaha pe main game loop chalega
# Isme hum user input lenge aur scenes switch karenge

from game.scenes import scenes
from game.inventory import player_inventory

class Game:
    def __init__(self):
        self.current_scene = scenes["dark_room"]
        self.game_over = False

    def run(self):
        while not self.game_over:
            self.display_scene()
            choice = self.get_player_choice()
            self.process_choice(choice)

    def display_scene(self):
        print("\n" + self.current_scene["description"])
        if "items" in self.current_scene:
            print(f"You see: {', '.join(self.current_scene['items'])}")
        if "npcs" in self.current_scene:
            for npc in self.current_scene["npcs"]:
                print(npc.description)
        for i, option in enumerate(self.current_scene["options"], 1):
            print(f"{i}. {option['text']}")

    def get_player_choice(self):
        return input("\nEnter choice: ").lower()

    def process_choice(self, choice):
        if choice == "quit":
            print("Thanks for playing!")
            self.game_over = True
            return
        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(self.current_scene["options"]):
                option = self.current_scene["options"][choice_idx]
                if "item_required" in option and not player_inventory.has_item(option["item_required"]):
                    print(f"You need a {option['item_required']}!")
                    return
                if "add_item" in option:
                    player_inventory.add_item(option["add_item"])
                    print(f"Picked up: {option['add_item']}")
                if option["next"] is None:
                    print(option.get("end_message", "Game Over!"))
                    self.game_over = True
                else:
                    self.current_scene = option["next"]
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter a number or 'quit'.")