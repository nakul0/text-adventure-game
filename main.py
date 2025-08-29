
# Yeh main file hai — yahin se game start hota hai. (Hinglish comment)
# Agar aap terminal se run karenge to yeh file execute hogi.

from game.engine import Game   # Game loop engine import kar rahe

def main():
    print("🎮 Welcome to the Text Adventure!")
    # Player ko bata rahe hain kaise exit karna hai
    print("Type 'quit' to exit.")
    game = Game()  # Game object banaya
    # Game loop start karo
    game.run()

if __name__ == "__main__":
    # Agar directly run ho raha hai to main() call karo
    main()