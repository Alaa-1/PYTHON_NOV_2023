from game_classes.human import Human

# print(Human)


# create a new class that inherits from class Human
# Inheritance
class Warrior(Human):
    def __init__(self, name):
        super().__init__(name)
        self.damage_multiplier = 5

    def attack(self, enemy):
        print(f"[WARRIOR ATTACK] {self.name} is attacking {enemy.name}")
        enemy.health -= self.strength * self.damage_multiplier
        print(f"{enemy.name} has {enemy.health} HP left.")

    def rage_attack(self, enemy):
        print(f"[RAGE ATTACK] {self.name} is rage atttacking {enemy.name}")
        enemy.health = 0
        print(f"{enemy.name} has {enemy.health} HP left.")


# warrior1 = Warrior("Morpheus")
# warrior2 = Warrior("Yasuo")


# warrior2.rage_attack(warrior1)
# if __name__ == "warrior":
#     print("Start the server !!")
