# Engine file: yaha pe main game loop chalega
# Isme hum user input lenge aur scenes switch karenge

from game.scenes import scenes
from game.inventory import player_inventory

# Thode se Hinglish synonyms: player Hindi/Roman words bhi type kar sake
HINGLISH_MAP = {
    "north": ["north", "n", "uttar", "upar", "aage", "aagey"],
    "south": ["south", "s", "dakkhin", "neeche", "peeche"],
    "pick": ["pick", "pick up", "pickup", "uthao", "utha", "le lo", "lelo"],
    "quit": ["quit", "exit", "chhoddo", "nikal", "bahar"]
}


class Game:
    def __init__(self):
        # scenes dict in game.scenes stores scene dictionaries; start in dark_room
        self.current_scene = scenes["dark_room"]
        self.game_over = False

    def run(self):
        while not self.game_over:
            self.display_scene()
            choice = self.get_player_choice()
            self.process_choice(choice)

    def display_scene(self):
        # Scene ka description print karo
        print("\n" + self.current_scene["description"])
        # Agar items hain to dikhao (jaise Rusty Key)
        if "items" in self.current_scene:
            print(f"You see: {', '.join(self.current_scene['items'])}")
        # NPC descriptions bhi print kar denge
        if "npcs" in self.current_scene:
            for npc in self.current_scene["npcs"]:
                print(npc.description)
        # Options ko number ke saath show karo
        for i, option in enumerate(self.current_scene["options"], 1):
            print(f"{i}. {option['text']}")

    def get_player_choice(self):
        # Player input lo; lower karke compare karenge
        return input("\nEnter choice: ").strip().lower()

    def _resolve_next_scene(self, next_ref):
        # next_ref string ho sakta hai (scene key) ya woh khud scene dict bhi ho sakta hai
        if next_ref is None:
            return None
        if isinstance(next_ref, str):
            return scenes.get(next_ref)
        return next_ref

    def _match_option_by_text(self, choice_text):
        # User ke text ko options se match karne ki koshish (Hinglish bhi chalega)
        tokens = [t for t in choice_text.split() if t]
        for i, option in enumerate(self.current_scene["options"]):
            opt_text = option.get("text", "").lower()
            # exact/substring match
            if choice_text in opt_text:
                return i
            # token match
            for t in tokens:
                if t in opt_text:
                    return i
            # check synonyms mapping
            for syn_list in HINGLISH_MAP.values():
                for syn in syn_list:
                    if syn in choice_text and syn in opt_text:
                        return i
        return None

    def process_choice(self, choice):
        # Quit ke kuch synonyms accept kar lo
        if choice in HINGLISH_MAP["quit"]:
            print("Thanks for playing!")
            self.game_over = True
            return

        # Agar player number type kare to us option ko use karenge
        try:
            choice_idx = int(choice) - 1
            matched_idx = choice_idx
        except ValueError:
            # Text se match karke option dhundo (Hinglish allowed)
            matched_idx = self._match_option_by_text(choice)

        if matched_idx is None:
            # User guidance message (Hinglish mix allowed)
            print("Enter a valid number, a direction (e.g. 'north' / 'upar'), or 'quit' (chhoddo).")
            return

        if 0 <= matched_idx < len(self.current_scene["options"]):
            option = self.current_scene["options"][matched_idx]
            # Agar kisi item ki zarurat hai to check karo
            if "item_required" in option and not player_inventory.has_item(option["item_required"]):
                print(f"You need a {option['item_required']}!")
                return
            # Agar option koi item deta hai to inventory mein add karo
            if "add_item" in option:
                player_inventory.add_item(option["add_item"])
                print(f"Picked up: {option['add_item']}")
            # Next scene resolve karo (string keys handle kar rahe)
            next_scene = self._resolve_next_scene(option.get("next"))
            if next_scene is None:
                print(option.get("end_message", "Game Over!"))
                self.game_over = True
            else:
                # Scene switch karo
                self.current_scene = next_scene
        else:
            print("Invalid choice.")