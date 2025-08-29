from game.engine import Game   # Game loop engine import kar rahe

def main():
    print("🎮 Welcome to the Text Adventure!")
    print("Type 'quit' to exit.")
    game = Game()  # Game object banaya
    game.run()

if __name__ == "__main__":
    main()