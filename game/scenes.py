# Yaha pe saare game scenes (rooms ya situations) define karenge
# Har scene ek dictionary hai with description aur options

# scenes.py
# This file defines all the scenes (rooms) of the adventure.

from game.characters import merchant, guard

dark_room = {
    # Yaha pe saare game scenes (rooms ya situations) define karenge
    # Har scene ek dictionary hai with description aur options (Hinglish comment)
    "description": "You're in a dark room with a door to the north.",
    "options": [
        {"text": "Go north", "next": "forest"}
    ]
}

forest = {
    "description": "A spooky forest surrounds you. Paths lead north and south.",
    "items": ["Rusty Key"],
    "options": [
        {"text": "Pick up Rusty Key", "add_item": "Rusty Key", "next": "forest"},
        {"text": "Go north", "next": "cave"},
        {"text": "Go south", "next": "village"}
    ]
}

cave = {
    "description": "A dark cave. A monster lurks inside.",
    "options": [
        {"text": "Fight monster", "item_required": "Sword", "next": "village", "end_message": "You defeated the monster!"},
        {"text": "Run away", "next": "forest", "end_message": "The monster ate you! Game Over!"}
    ]
}

village = {
    "description": "A quiet village with a merchant and a path to the castle.",
    "npcs": [merchant],
    "items": ["Sword"],
    "options": [
        {"text": "Pick up Sword", "add_item": "Sword", "next": "village"},
        {"text": "Go north", "next": "castle"},
        {"text": "Go north", "next": "forest"}
    ]
}

castle = {
    "description": "A grand castle. A guard blocks a treasure chest.",
    "npcs": [guard],
    "options": [
        {"text": "Unlock chest", "item_required": "Rusty Key", "next": None, "end_message": "You found the treasure! You win!"},
        {"text": "Talk to guard", "next": "castle", "end_message": "The guard won't let you pass."}
    ]
}

scenes = {
    "dark_room": dark_room,
    "forest": forest,
    "cave": cave,
    "village": village,
    "castle": castle
}