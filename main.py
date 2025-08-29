# Ye game ka entry point hai (yaha se game start hoga)
# Just ek line me game start karenge using Game class

from game.engine import Game  # Game loop engine import kar rahe

if __name__ == "__main__":
    game = Game()   # Game object banaya
    game.start()    # Game ko start kiya
