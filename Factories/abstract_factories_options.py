<<<<<<< HEAD
from abc import ABC,abstractmethod
from enum import Enum,auto




class HotDrink(ABC):
    @abstractmethod
    def consume(self):
        pass
    @abstractmethod
    def sugar(self,amount):
        pass


class Coffee(HotDrink):
    def sugar(self,amount):
        self.amount= amount
        print(f"Sugar {self.amount}")
        return self
        
    def consume(self):
        print(f"Wow This {self.__class__.__name__} is Delicions")
    
class Tea(HotDrink):
    def sugar(self,amount):
        self.amount= amount
        print(f"Sugar {self.amount}")
        return self
    
    def consume(self):
        print(f"Wow This {self.__class__.__name__} is Delicions")


class HotDrinkFactory(ABC):
    def prepare(self,amount):
        pass


class CoffeeFactory(HotDrinkFactory):
    def prepare(self,amount):
        print(f"preparing {amount} ml of Coffee")
        return Coffee()


class TeaFactory(HotDrinkFactory):
    def prepare(self,amount):
        print(f"preparing {amount} ml of Tea")
        return Tea()

def make_drink(type):
    if type == "tea":
        return TeaFactory().prepare(40)
    elif type == "coffee":
        return CoffeeFactory().prepare(20)
    else:
        return None


class HotDrinkMachine:
    class AvailbaleDrink(Enum):
        COFFEE = auto()
        TEA = auto()
    factories = []
    inistantiated = False

    def __init__(self):
        self.inistantiated= True
        for drink in self.AvailbaleDrink:
            name = drink.name[0].upper() + drink.name[1:].lower()
            factory_name = name +"Factory"
            factory_object = eval(factory_name)()
            self.factories.append((name,factory_object))
    
    def make_drink(self):
        print("Available Drinks")
        for f in self.factories:
            print(f[0])
        drink_idx = int(input(f"Please Choose Drink from (0 to {len(self.factories)-1}) : "))
        amount = int(input("Please enter amount : "))
        sugar_amount = int(input("Please enter sugar amount : "))
        self.factories[drink_idx][1].prepare(amount).sugar(sugar_amount).consume()
    

=======
from abc import ABC,abstractmethod
from enum import Enum,auto




class HotDrink(ABC):
    @abstractmethod
    def consume(self):
        pass
    @abstractmethod
    def sugar(self,amount):
        pass


class Coffee(HotDrink):
    def sugar(self,amount):
        self.amount= amount
        print(f"Sugar {self.amount}")
        return self
        
    def consume(self):
        print(f"Wow This {self.__class__.__name__} is Delicions")
    
class Tea(HotDrink):
    def sugar(self,amount):
        self.amount= amount
        print(f"Sugar {self.amount}")
        return self
    
    def consume(self):
        print(f"Wow This {self.__class__.__name__} is Delicions")


class HotDrinkFactory(ABC):
    def prepare(self,amount):
        pass


class CoffeeFactory(HotDrinkFactory):
    def prepare(self,amount):
        print(f"preparing {amount} ml of Coffee")
        return Coffee()


class TeaFactory(HotDrinkFactory):
    def prepare(self,amount):
        print(f"preparing {amount} ml of Tea")
        return Tea()

def make_drink(type):
    if type == "tea":
        return TeaFactory().prepare(40)
    elif type == "coffee":
        return CoffeeFactory().prepare(20)
    else:
        return None


class HotDrinkMachine:
    class AvailbaleDrink(Enum):
        COFFEE = auto()
        TEA = auto()
    factories = []
    inistantiated = False

    def __init__(self):
        self.inistantiated= True
        for drink in self.AvailbaleDrink:
            name = drink.name[0].upper() + drink.name[1:].lower()
            factory_name = name +"Factory"
            factory_object = eval(factory_name)()
            self.factories.append((name,factory_object))
    
    def make_drink(self):
        print("Available Drinks")
        for f in self.factories:
            print(f[0])
        drink_idx = int(input(f"Please Choose Drink from (0 to {len(self.factories)-1}) : "))
        amount = int(input("Please enter amount : "))
        sugar_amount = int(input("Please enter sugar amount : "))
        self.factories[drink_idx][1].prepare(amount).sugar(sugar_amount).consume()
    

>>>>>>> 2c05466 (adding new designs)
HotDrinkMachine().make_drink()