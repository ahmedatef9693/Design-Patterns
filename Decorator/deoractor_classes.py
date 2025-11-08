class Coffee:
    def __init__(self):
        self.description = "Coffee"
        self.cost = 5
    def get_cost(self):
        return self.cost


class CoffeeDecorator:
    def __init__(self,coffee:Coffee):
        self.coffee = coffee
    
    def get_cost(self):
        return self.coffee.get_cost()
        

class SugerDecorator(CoffeeDecorator):
    def get_cost(self):
        return self.coffee.get_cost() + 2

    def __str__(self):
        return f"Price Of Coffee {self.coffee.get_cost()+2}"
    
class MilkDecorator(CoffeeDecorator):
    def get_cost(self):
        return self.coffee.get_cost() + 3

    def __str__(self):
        return f"Price Of Coffee {self.coffee.get_cost()+3}"

sugarmilk_coffee = MilkDecorator(SugerDecorator(Coffee()))
print(sugarmilk_coffee)
