# Yaha pe saare game scenes (rooms ya situations) define karenge
# Har scene ek dictionary hai with description aur options

# scenes.py
# This file defines all the scenes (rooms) of the adventure.

# Final winning scene
treasure_room = {
    "description": "\n✨ You enter a shining treasure room filled with gold and jewels. You WIN! ✨",
    "options": [
        {"text": "Quit the game", "next": None}
    ]
}

# Danger scene
monster_room = {
    "description": "\n👹 A scary monster appears! You try to fight but it defeats you. GAME OVER.",
    "options": [
        {"text": "Quit the game", "next": None}
    ]
}

# Forest scene
forest_scene = {
    "description": "\n🌲 You are standing in a spooky forest. Paths lead north and east.",
    "options": [
        {"text": "Go north (towards treasure)", "next": treasure_room},
        {"text": "Go east (towards danger)", "next": monster_room},
        {"text": "Go back south (to start)", "next": None}  # optional back link
    ]
}

# Starting scene
start_scene = {
    "description": "\n😴 You wake up in a dark room. There's a door to the north.",
    "options": [
        {"text": "Open the door", "next": forest_scene},
        {"text": "Stay in the room", "next": None}
    ]
}


# Example: future me aur scenes add karna
# hallway_scene = {
#     "description": "Aap ek hallway me enter karte ho, jisme torches lagi hai.",
#     "options": [
#         {"text": "Left me jao", "next": another_scene},
#         {"text": "Right me jao", "next": yet_another_scene}
#     ]
# }
