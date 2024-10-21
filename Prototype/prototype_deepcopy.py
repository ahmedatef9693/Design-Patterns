

from copy import deepcopy



class Person:
    def __init__(self,name,address):
        self.name = name
        self.address = address


    def __str__(self) -> str:
        return f'{self.name} , {self.address}'



class Address:
    def __init__(self,street_name,city,country):
        self.street_name = street_name
        self.city = city
        self.country = country

    def __str__(self) -> str:
        return f'{self.street_name} , {self.city} , {self.country}'





john = Person("John",Address("123","London","UK"))
jane = deepcopy(john)
jane.address = Address("123b","London","UK")
jane.address.city = "cairo"
jane.address.country = "Egypt" 

print(john)
print(jane)




