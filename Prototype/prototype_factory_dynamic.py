<<<<<<< HEAD

from copy import deepcopy

class Employee:
    def __init__(self):
        self.name = None
        self.address = None
        self.department = None
    def __str__(self):
        return f"""
        name {self.name}
        address : street : {self.address.street} , 
        block : {self.address.block} , 
        city : {self.address.city}"""

class Address:
    def __init__(self,street,block,city):
        self.street = street
        self.block = block
        self.city = city

class EmployeeBuilder(Employee):
    def __init__(self):
        self.employee = Employee()
    def called(self,name):
        self.employee.name = name
        return self
    def lives_in(self,address:Address):
        self.employee.address = address
        return self
    def build(self):
        return self.employee




# emp = EmployeeBuilder().called("ahmed").lives_in(Address("s","f","cairo")).build()
# print(emp)




class Accountant(EmployeeBuilder):
    def __init__(self, name, address):
        super().__init__(name, address)

class SoftwareEngineer(EmployeeBuilder):
    def solve_problem(self):
        print("Solving Problem")
    def make_application(self):
        print("Making Application")
    def test_application(self):
        print("Testing Application")

class Teacher(Employee):
    def __init__(self,name:str,address:Address,department:str):
        self.name = name
        self.address = address
        self.department = department
    


# ProtoType Pattern
class EmployeeFactory:

    math_teacher = Teacher("samy",Address("badr","3","cairo"),"Math")
    biology_teacher = Teacher("mohamed",Address("badr2","32","qalyubia"),"Biology")


    @staticmethod
    def create_employee(employee_type):
        if employee_type == "Finance":
            return Accountant().called("mo").lives_in(Address("fas","sssa","kalub")).build()
        elif employee_type == "Engineer":
            return SoftwareEngineer().called("sozan").lives_in(Address("s","f","cairo")).build()

    @staticmethod
    def __create_proto_teacher(proto,name:str,address:Address)->Teacher:
        teacher = deepcopy(proto)
        teacher.name = name
        teacher.address = address
        return teacher


    @staticmethod
    def create_biology_teacher(name,address):
        return EmployeeFactory.__create_proto_teacher(
            EmployeeFactory.biology_teacher,
            name,address
        )
        

    @staticmethod
    def create_math_teacher(name,address):
        return EmployeeFactory.__create_proto_teacher(
            EmployeeFactory.math_teacher,
            name,address
        )


# print(EmployeeFactory.create_employee(employee_type="Engineer"))

=======

from copy import deepcopy

class Employee:
    def __init__(self):
        self.name = None
        self.address = None
        self.department = None
    def __str__(self):
        return f"""
        name {self.name}
        address : street : {self.address.street} , 
        block : {self.address.block} , 
        city : {self.address.city}"""

class Address:
    def __init__(self,street,block,city):
        self.street = street
        self.block = block
        self.city = city

class EmployeeBuilder(Employee):
    def __init__(self):
        self.employee = Employee()
    def called(self,name):
        self.employee.name = name
        return self
    def lives_in(self,address:Address):
        self.employee.address = address
        return self
    def build(self):
        return self.employee




# emp = EmployeeBuilder().called("ahmed").lives_in(Address("s","f","cairo")).build()
# print(emp)




class Accountant(EmployeeBuilder):
    def __init__(self, name, address):
        super().__init__(name, address)

class SoftwareEngineer(EmployeeBuilder):
    def solve_problem(self):
        print("Solving Problem")
    def make_application(self):
        print("Making Application")
    def test_application(self):
        print("Testing Application")

class Teacher(Employee):
    def __init__(self,name:str,address:Address,department:str):
        self.name = name
        self.address = address
        self.department = department
    


# ProtoType Pattern
class EmployeeFactory:

    math_teacher = Teacher("samy",Address("badr","3","cairo"),"Math")
    biology_teacher = Teacher("mohamed",Address("badr2","32","qalyubia"),"Biology")


    @staticmethod
    def create_employee(employee_type):
        if employee_type == "Finance":
            return Accountant().called("mo").lives_in(Address("fas","sssa","kalub")).build()
        elif employee_type == "Engineer":
            return SoftwareEngineer().called("sozan").lives_in(Address("s","f","cairo")).build()

    @staticmethod
    def __create_proto_teacher(proto,name:str,address:Address)->Teacher:
        teacher = deepcopy(proto)
        teacher.name = name
        teacher.address = address
        return teacher


    @staticmethod
    def create_biology_teacher(name,address):
        return EmployeeFactory.__create_proto_teacher(
            EmployeeFactory.biology_teacher,
            name,address
        )
        

    @staticmethod
    def create_math_teacher(name,address):
        return EmployeeFactory.__create_proto_teacher(
            EmployeeFactory.math_teacher,
            name,address
        )


# print(EmployeeFactory.create_employee(employee_type="Engineer"))

>>>>>>> 2c05466 (adding new designs)
print(EmployeeFactory.create_biology_teacher("ahmed",Address("s","f","q")))