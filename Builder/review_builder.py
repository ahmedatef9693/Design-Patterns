from enum import Enum
from datetime import datetime

class MilatryStatus(Enum):
    COMPLETED = 0
    EXEMPTED = 1
    POSTPONED = 2
    TEMPORARY_EXEMPTED = 3




class Person:
    def __init__(self):
        
        #person details
        self.first_name = None
        self.last_name = None
        self.national_id = None
        self.gender = None
        self.religion = None
        self.date_of_birth = None
        self.full_name = None
        self.mobile_no = None
        self.street_address = None
        self.city = None
        #employment details
        self.is_employed = None
        self.milatary_status = None
        self.date_of_joining = None
        self.department = None
        self.position = None
        self.branch = None
        self.reports_to = None
        print("called")
    def __str__(self):
        return f"""
         -----------------
        |'Person Details'|
         -----------------
         Name : {self.full_name}
         Address : {self.street_address} {self.city}
         mobile_no : {self.mobile_no} 
         gender : {self.gender}
         national_id : {self.national_id}
         position : {self.position}
         date of joinning : {self.date_of_joining}
         department : {self.department}
         branch : {self.branch}
         reports_to : {self.reports_to}
        """


class PersonBuilder:
    def __init__(self):
        self.person = Person()
    def build(self):
        return self.person
    

class PersonalDetailsBuilder(PersonBuilder):
    def phone(self,mobile_no):
        self.person.mobile_no = mobile_no
        return self

    def name (self,first_name,last_name):
        self.person.first_name = first_name
        self.person.last_name = last_name
        self.person.full_name = str(self.person.first_name) + str(self.person.last_name)
        return self

    def religion(self,religion):
        self.person.religion = religion
        return self
    
    def gender_type(self,gender):
        self.person.gender = gender
        return self
    
    def born_in(self,city):
        self.person.city = city
        return self
    
    def dob(self,date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self
    
    def at(self,street_address):
        self.person.street_address = street_address
        return self
    def validate_ssn(self,ssn):
        if len(ssn) < 14:
            raise Exception("Sorry, National Id Is less than 14 characters")

    def SSN(self,national_id):
        self.validate_ssn(national_id)
        self.person.national_id = national_id
        return self


class JobDetailsBuilder(PersonalDetailsBuilder):
    def works_as(self,position):
        self.person.position = position
        if position:
            self.__is_employed(True)
        self.__set_joining_date()
        return self
    
    def __is_employed(self,is_employed):
        self.person.is_employed = is_employed
    
    def milatary_status(self,status):
        self.person.milatary_status = status
        return self
    
    def __set_joining_date(self):
        self.person.date_of_joining = datetime.now()

    def department(self,department):
        self.person.department = department
        return self
    
    def branch(self,branch):
        self.person.branch = branch
        return self
    
    def reports_to(self,person):
        self.person.reports_to = person
        return self




pb = JobDetailsBuilder()
person_details = pb.\
    name("Jack","Greilish").\
    phone("01159607829").\
    dob("15/5/2005").\
    born_in("cairo").\
    at("125street").\
    gender_type("Male").\
    religion("Muslim").\
    SSN("12345678910112").\
    works_as("Software Developer").\
    milatary_status(MilatryStatus.COMPLETED).\
    department("SW").\
    branch("Ainshams").\
    reports_to("Fredrick").\
    build()


print(person_details)