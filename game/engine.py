# Engine file: yaha pe main game loop chalega
# Isme hum user input lenge aur scenes switch karenge

from game import scenes

class Game:
    def __init__(self):
        self.current_scene = scenes.start_scene   # Starting scene set kiya
        self.is_running = True                    # Game chal raha hai ya nahi
        self.inventory = []                       # Player ka inventory list

    def start(self):
        print("🎮 Welcome to the Text Adventure Game!")
        print("Type 'quit' to exit.\n")

        # Jab tak game chal raha hai, har turn chalti rahegi
        while self.is_running:
            self.play_turn()

    def play_turn(self):
        # Scene ka description print karo
        print(self.current_scene["description"])

        # Options print karo
        for i, option in enumerate(self.current_scene["options"], 1):
            print(f"{i}. {option['text']}")

        # User input lo
        choice = input("\nType here: ").strip().lower()

        if choice == "quit":
            self.is_running = False
            print("\n👋 Thanks for playing!")
            return

        # User choice handle karo
        try:
            choice_idx = int(choice) - 1
            selected_option = self.current_scene["options"][choice_idx]
            self.current_scene = selected_option["next"]
        except (ValueError, IndexError):
            print("\n⚠️!\n")
