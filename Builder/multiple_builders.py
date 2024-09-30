class Person:
    def __init__(self):
        #name
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        #address
        self.street_address = None
        self.postcode = None
        self.city = None
        #employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return f""" 
         Name {self.first_name} {self.middle_name} {self.last_name} 
         Address {self.street_address} {self.city} {self.postcode}
         Employed At {self.company_name} as a {self.position} earning {self.annual_income}
        """




class PersonBuilder:
    def __init__(self,person = Person()):
        self.person = person
    
    @property
    def has(self):
        return PersonNameBuilder(self.person)
    @property
    def works(self):
        return PersonJobBuilder(self.person)
    @property
    def lives(self):
        return PersonAddressBuilder(self.person)
    def build(self):
        return self.person





class PersonJobBuilder(PersonBuilder):
    def __init__(self,person):
        super().__init__(person)
    
    def at(self,company_name):
        self.person.company_name = company_name
        return self
    def as_a(self,position):
        self.person.position = position
        return self
    def earning(self,annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self,person):
        super().__init__(person)
    
    def at(self,street_address):
        self.person.street_address = street_address
        return self
    def in_city(self,city):
        self.person.city = city
        return self
    def with_postal_code(self,postal_code):
        self.person.postcode = postal_code
        return self



class PersonNameBuilder(PersonBuilder):
    def __init__(self,person):
        super().__init__(person)
    def name(self,first_name,middle_name,last_name):
        self.person.first_name = first_name
        self.person.middle_name = middle_name
        self.person.last_name = last_name
        return self

pb = PersonBuilder()
person = pb.\
            has.\
                name("Mike","T","Tyson").\
            lives.\
                at("London 123st").\
                in_city("London").\
                with_postal_code("1245ssw").\
            works.\
                at("CIB").\
                as_a("Software Developer").\
                earning(5000).\
            build()
print(person)