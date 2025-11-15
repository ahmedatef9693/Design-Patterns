class Character:
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost
    def get_cost(self):
        return self.cost

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, cost=120)

class Dwarf(Character):
    def __init__(self, name):
        super().__init__(name, cost=80) 

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, cost=100)

class RpgDecorator:
    def __init__(self,character:Character):
        self.character = character
    def get_cost(self):
        return self.character.get_cost()

    def get_base_character(self):
        current = self.character
        while isinstance(current,RpgDecorator):
            print(f"curent object of type {current}")
            current = current.character
        return current




class Shield(RpgDecorator):
    def __init__(self, character):
        super().__init__(character)
    def get_cost(self):
        return self.character.get_cost() + 20

class MagicBoost(RpgDecorator):
    def get_cost(self):
        return self.character.get_cost() + 50


class PoisonResistance(RpgDecorator):
    def __init__(self, character):
        super().__init__(character)
    
    def get_poison_resistence(self):
        character = self.get_base_character()
        if isinstance(character , Warrior):
            return 50
        elif isinstance(character , Archer):
            return 100
        elif isinstance(character , Dwarf):
            return 10
        else:
            return 0
    def get_cost(self):
        return self.character.get_cost() + self.get_poison_resistence()


print(PoisonResistance(MagicBoost(Shield(Warrior("Warrior 1")))).get_cost())