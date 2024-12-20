
from copy import deepcopy

class Address:
    def __init__(self,street_address,suite,city):
        self.street_address = street_address
        self.suite = suite
        self.city = city
    
    def __str__(self) -> str:
        return f'{self.street_address} , {self.suite} , {self.city}'
    


class Employee:
    def __init__(self,name,address):
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f'{self.name} , {self.address}'
    


class EmployeeFactory:
    main_office_employee = Employee("",Address("123A East",0,"Cairo"))
    aux_office_employee = Employee("",Address("123B East",0,"Cairo"))



    def __new_employee(prototype,name,suite):
        result_copy = deepcopy(prototype)
        result_copy.name = name
        result_copy.address.suite = suite
        return result_copy


    @staticmethod
    def new_main_office(name,suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name,
            suite
        )

    @staticmethod
    def new_aux_office(name,suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name,
            suite
        )



ahmed = EmployeeFactory.new_main_office("ahmed",5)
kareem = EmployeeFactory.new_aux_office("kareem",10)
print(ahmed)
print(kareem)
        