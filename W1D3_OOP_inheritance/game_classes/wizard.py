from game_classes.human import Human


class Wizard(Human):
    def __init__(self, name, mana, spells):
        super().__init__(name)
        self.mana = mana
        self.spells = spells
