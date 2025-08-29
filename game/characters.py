# Characters (NPCs ya enemies) yaha define karenge

class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description

merchant = Character("Merchant", "A friendly merchant offers you a hint: 'Find the key!'")
guard = Character("Guard", "A tall guard blocks the treasure chest.")