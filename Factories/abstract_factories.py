from abc import ABC

class HotDrink(ABC):
    def consume(self):
        pass


class Coffee(HotDrink):
    def consume(self):
        print("Coffee Drink Is So Deleicious!")


class Tea(HotDrink):
    def consume(self):
        print("Teas Is So Deleicious!")



class HotDrinkFactory(ABC):
    def prepare(self,amount):
        pass

class CoffeeFactory(HotDrinkFactory):
    def prepare(self,amount):
        print(f"Grind Beans , Boil Water , Pour {amount}ml ,enjoy!")
        return Coffee()


class TeaFactory(HotDrinkFactory):
    def prepare(self,amount):
        print(f"Put In Tea Bag , Boil Water , Pour {amount}ml ,enjoy!")
        return Tea()


def make_drink():
    drink = input("Enter Your Drink : ")
    if drink == "tea":
        return TeaFactory().prepare(100)
    elif drink == "coffee":
        return CoffeeFactory().prepare(50)
    

make_drink().consume()

