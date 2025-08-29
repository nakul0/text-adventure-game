# Characters (NPCs ya enemies) yaha define karenge
# Yeh file NPCs ke naam aur unki description rakhti hai (Hinglish comment)


class Character:
    def __init__(self, name, description):
        # NPC ka simple constructor: name aur description store karo
        self.name = name
        self.description = description


merchant = Character("Merchant", "A friendly merchant offers you a hint: 'Find the key!'")
guard = Character("Guard", "A tall guard blocks the treasure chest.")