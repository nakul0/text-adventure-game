# 🎮 Text Adventure Game (Template)

This is a simple **text-based adventure game** boilerplate written in Python.  
You and your friends can use this template to easily build your own **story-driven terminal adventure game**.

---

## 🚀 How to Run the Game
1. Make sure you have **Python 3.8+** installed.  
   To check:
   ```bash
   python --version
or

bash
Copy code
python3 --version
Clone this repository (or download the ZIP and extract it):

bash
Copy code
git clone https://github.com/YOUR-USERNAME/text-adventure-game.git
cd text-adventure-game
Run the game:

bash
Copy code
python main.py
📂 Project Structure
bash
Copy code
text-adventure-game/
│
├── game/
│   ├── __init__.py       # Marks this folder as a Python package
│   ├── engine.py         # Main game loop logic (input, output, switching scenes)
│   ├── scenes.py         # Define different rooms/scenes of the game
│   ├── characters.py     # Define characters/NPCs
│   └── inventory.py      # Simple inventory system
│
├── main.py               # Entry point of the game (run this file)
├── README.md             # Documentation
└── requirements.txt      # Python dependencies (currently empty)
🛠️ How to Add Your Own Content
1. Add a New Scene
Go to game/scenes.py and define a new scene as a dictionary:

python
Copy code
forest_scene = {
    "description": "You are standing in a spooky forest with trees all around.",
    "options": [
        {"text": "Go north", "next": cave_scene},
        {"text": "Go south", "next": start_scene}
    ]
}
description → Text shown to the player.

options → Choices available to the player. Each option has:

"text" → What the player sees.

"next" → Which scene to go to after choosing.

⚠️ Note: You must define the next scene somewhere in scenes.py (otherwise it will be None and the game will stop).

2. Link Scenes Together
Example:

python
Copy code
start_scene = {
    "description": "You wake up in a dark room. There’s a door to the north.",
    "options": [
        {"text": "Open the door", "next": forest_scene},
        {"text": "Stay in the room", "next": None}
    ]
}
Here, if the player chooses "Open the door", the game moves to forest_scene.

3. Add Characters
Open game/characters.py and define NPCs (non-player characters):

python
Copy code
from game.characters import Character

guard = Character("Guard", "A tall man with a sword, blocking your way.")
4. Add Inventory Items
Open game/inventory.py to manage items:

python
Copy code
from game.inventory import Inventory

player_inventory = Inventory()
player_inventory.add_item("Rusty Key")
player_inventory.show_inventory()
✅ Next Steps
Create at least 5 interconnected scenes (to make the story interesting).

Add items (like keys, potions, weapons) that players can collect.

Add NPCs (friendly or enemies) for interactions.

Add winning and losing conditions (for example: finding treasure = win, getting caught by monster = lose).

📖 Example Gameplay
vbnet
Copy code
🎮 Welcome to the Text Adventure Game!
Type 'quit' anytime to exit.

You wake up in a dark room. There's a door to the north.
1. Open the door
2. Stay in the room

Enter your choice: 1
You are standing in a spooky forest with trees all around.
1. Go north
2. Go south