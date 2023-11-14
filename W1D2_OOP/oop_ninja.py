class Ninja:
    # class attributes
    list_of_ninjas = []

    # Constructor
    def __init__(self, name: str, weapon, age, health, belt, strength):
        # Attributes
        self.name = name
        self.weapon = weapon
        self.age = age
        self.health = health
        self.belt = belt
        self.strength = strength
        Ninja.list_of_ninjas.append(self)

    # def __repr__(self):
    #     return f"This is a ninja and his name is {self.name}"

    # Instance Methods
    def display_stats(self):
        print(
            f"{self.name} is a {self.belt} ninja\nwith a {self.weapon}\nand health of {self.health} HP"
        )

    def eat_pizza(self):
        self.health += 10
        print(f"{self.name} ate a pizza and their health is now {self.health} HP")

    def attack(self, target):
        target.health -= self.strength
        print(
            f"{self.name} attacks {target.name} with a {self.strength} DM and they are left with {target.health} HP"
        )
        # print(self)
        return self

    # annotation (decorator)
    @classmethod
    def party(cls):
        for one_ninja in cls.list_of_ninjas:
            one_ninja.eat_pizza()

    @staticmethod
    def check_age(ninjaAge):
        is_valid = True
        if ninjaAge < 18:
            is_valid = False
            print("You are not old enough to become a Ninja !!")
        return is_valid


# Create an Instance
ninja1 = Ninja("Donatelo", "Bo Stuff", 18, 1000, "Blue", 90)
villain = Ninja("Shredder", "Armor", 5, 2000, "Black", 990)
# print(ninja1)
# villain.display_stats()
# # ninja1.eat_pizza()
# print("=" * 30)
# ninja1.attack(villain)
# # ninja1.attack(villain)
# # ninja1.attack(villain)
# print("=" * 30)
# villain.display_stats()

# print(Ninja.list_of_ninjas)

# villain.display_stats()
# ninja1.display_stats()
# print("=" * 30)
# Ninja.party()
# ninja1.display_stats()
# print("=" * 30)
# villain.display_stats()

print(Ninja.check_age(villain.age))


# / Classmethod
""""
do not have access to the instance
no self instread use cls
can only be called from the class
"""

# > Staticmethod

""""
independent
-- Utility functions (methods)
"""
