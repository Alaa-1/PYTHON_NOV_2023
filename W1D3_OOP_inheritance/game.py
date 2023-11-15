from game_classes.warrior import Warrior
from game_classes.wizard import Wizard


warrior1 = Warrior("Zac")
wizard1 = Wizard("Yoni", 6, "Wind Style")

while warrior1.health > 0 and wizard1.health > 0:
    print("Choose you character:\n ")
    response = ""

    response = input("1)Wizard\n2)Warrior \n")

    if response == "1":
        print("Do you want to attack ⚔??")
        res = input("Y/N :")
        if res == "Y":
            wizard1.attack(warrior1)
        else:
            warrior1.attack(wizard1)
    elif response == "2":
        print("Do you want to attack ??")
        res = input("Y/N :")
        if res == "Y":
            warrior1.attack(wizard1)
        else:
            wizard1.attack(warrior1)

    else:
        print("Wrong Choice ! Try Again")

print("Game Over 😥")
