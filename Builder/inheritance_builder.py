class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None
    def __str__(self) -> str:
        return f"""
            name is {self.name} works as {self.position} born in {self.date_of_birth}
        """


class PersonBuilder:
    def __init__(self):
        self.person = Person()
    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):    
    def called(self,name):
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder):
    def works_as(self,job):
        self.person.position = job
        return self
    
class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self,birth_date):
        self.person.date_of_birth = birth_date
        return self



pb = PersonBirthDateBuilder().\
    born("1/5/1996").\
    called("Jake").\
    works_as("software developer").\
    build()

print(pb)