<<<<<<< HEAD
class Resturnat:
    def __init__(self,pizza:Pizza):
        self.pizza = pizza

        
    def make(self):
        pass

class AmericanResturant(Resturnat):
    def __init__(sel,pizza:Pizza):
        super().__init__(pizza)
        
    def make(self):
        print(f"Making {self.pizza.__class__.__name__} in American Resturant")


class ItalianResturant(Resturnat):
    def __init__(self,pizza:Pizza):
        super().__init__(pizza)
        
    def make(self):
        print(f"Making {self.pizza.__class__.__name__} in Italian Resturant")

class Pizza:
    def __init__(self):
        pass
class CheesePizza(Pizza):
    def __init__(self):
        pass

class PepperoniPizza(Pizza):
    def __init__(self):
        pass


italian_resturant = ItalianResturant(PepperoniPizza())
american_resturant = AmericanResturant(CheesePizza())

italian_resturant.make()
=======
class Resturnat:
    def __init__(self,pizza:Pizza):
        self.pizza = pizza

        
    def make(self):
        pass

class AmericanResturant(Resturnat):
    def __init__(sel,pizza:Pizza):
        super().__init__(pizza)
        
    def make(self):
        print(f"Making {self.pizza.__class__.__name__} in American Resturant")


class ItalianResturant(Resturnat):
    def __init__(self,pizza:Pizza):
        super().__init__(pizza)
        
    def make(self):
        print(f"Making {self.pizza.__class__.__name__} in Italian Resturant")

class Pizza:
    def __init__(self):
        pass
class CheesePizza(Pizza):
    def __init__(self):
        pass

class PepperoniPizza(Pizza):
    def __init__(self):
        pass


italian_resturant = ItalianResturant(PepperoniPizza())
american_resturant = AmericanResturant(CheesePizza())

italian_resturant.make()
>>>>>>> 2c05466 (adding new designs)
american_resturant.make()