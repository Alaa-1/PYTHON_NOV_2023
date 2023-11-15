class Human:
    def __init__(self, name):
        self.name = name
        self.strength = 80
        self.health = 250
        self.defense = 50

    # attack
    def attack(self, enemy):
        print(f"[HUMAN ATTACK] {self.name} is attacking {enemy.name}")
        enemy.defend(self.strength)

    # taking damage
    def defend(self, damage):
        self.defense -= damage
        print(
            f"[HUMAN DEFEND] {self.name} takes {damage} DMG and they are now at {self.health} HP."
        )
