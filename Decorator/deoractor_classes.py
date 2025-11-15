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
    def __init__(self, coffee):
        super().__init__(coffee)
    
    def get_cost(self):
        return self.coffee.get_cost() + 2

    def __str__(self):
        return f"Price Of Sugar Coffee {self.coffee.get_cost()+2}"
    
class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
        # print("Sugar",self.coffee.get_cost())
    
    def get_cost(self):    
        return self.coffee.get_cost() + 3

    def __str__(self):
        return f"Price Of Milk Coffee {self.coffee.get_cost()+3}"

class TaxDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self):
        base = self.coffee.get_cost()
        tax:float = base + (base * 0.14)
        return tax
    
    def __str__(self):
        return f"Price Of Coffee After Tax {self.get_cost()}"


class DiscountDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
    
    def get_cost(self):
        base = self.coffee.get_cost()
        discount:float = base - (base * 0.1)
        return discount
    
    def __str__(self):
        return f"Price Of Coffee After Discount {self.get_cost()}"


print(DiscountDecorator(TaxDecorator(MilkDecorator(SugerDecorator(Coffee())))))