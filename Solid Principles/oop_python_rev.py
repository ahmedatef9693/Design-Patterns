
# # # # # def before_after_decorator(func):
# # # # #     def wrapper(*args,**kwargs):
# # # # #         print("before average")
# # # # #         if 'name' in kwargs:
# # # # #             print(kwargs['name'])
# # # # #         m = [v for v in args[0]]
# # # # #         print(m)
# # # # #         # print(kwargs.get('name'))
# # # # #         func(*args, **kwargs)
# # # # #         print("after average")
# # # # #     return wrapper

# # # # # @before_after_decorator
# # # # # def get_avg(prices , name ="Average"):
# # # # #     avg = sum(prices)/len(prices)
# # # # #     print(f'{avg}')
    
    
# # # # # prices = [120,12,30]
# # # # # get_avg(prices,name="Average")




# # # # class Parent:
# # # #     def __init__(self):
# # # #         self.public_var = "I am public"
# # # #         self._protected_var = "I am protected"
# # # #         self.__private_var = "I am private"

# # # #     def get_private_var(self):
# # # #         return self.__private_var

# # # # class ChildA(Parent):
# # # #     def __init__(self):
# # # #         super().__init__()
# # # #         self._protected_var = "Changed by ChildA"
# # # #         print("Accessing in ChildA:")


# # # # class ChildB(Parent):
# # # #     def __init__(self):
# # # #         super().__init__()


# # # # # Example usage
# # # # parent = Parent()
# # # # child_a = ChildA()
# # # # child_b = ChildB()
# # # # print(parent._protected_var)










# # # # class Parent:
# # # #     def __init__(self,val):
# # # #         self.public_var = "I am public"
# # # #         self._protected_var = "I am protected"
# # # #         self.__private_var = "I am private"
# # # #         self.val = val

# # # #     def get_private_var(self):
# # # #         return self.__private_var

# # # # class ChildA(Parent):
# # # #     def __init__(self,val):
# # # #         super().__init__(val)
# # # #         self._protected_var = "Changed by ChildA"
# # # #         print("Accessing in ChildA:")

# # # # class ChildB(Parent):
# # # #     def __init__(self,val):
# # # #         super().__init__(val)
# # # #         self._protected_var = "Changed by Childb"
# # # #         print("Accessing in Childb:")


# # # # # Example usage
# # # # parent = Parent(1)
# # # # child_a = ChildA(2)
# # # # child_b = ChildB(3)

# # # # # Accessing protected variable from different instances
# # # # print("Parent protected variable:", parent._protected_var)  # This will print: I am protected
# # # # print("ChildA protected variable:", child_a._protected_var)  # This will print: Changed by ChildA
# # # # print("ChildB protected variable:", child_b._protected_var)  # This will print: I am protected
# # # # print("Parent protected variable:", parent._protected_var)  # This will print: I am protected




# # # class Parent:
# # #     _protected_var = "I am protected"  # Class variable

# # #     def __init__(self):
# # #         self.public_var = "I am public"
# # #         self.__private_var = "I am private"

# # #     def get_private_var(self):
# # #         return self.__private_var

# # # class ChildA(Parent):
# # #     def __init__(self):
# # #         super().__init__()
# # #         Parent._protected_var = "Changed by ChildA"  # Change class variable
# # #         print("Accessing in ChildA:")

# # # class ChildB(Parent):
# # #     def __init__(self):
# # #         super().__init__()
# # #         Parent._protected_var = "Changed by ChildB"  # Change class variable

# # # # Example usage
# # # parent = Parent()
# # # child_a = ChildA()
# # # child_b = ChildB()

# # # # Accessing protected variable from different instances
# # # print("Parent protected variable:", Parent._protected_var)  # This will print: Changed by ChildA
# # # print("ChildA protected variable:", ChildA._protected_var)  # This will print: Changed by ChildA
# # # print("ChildB protected variable:", ChildB._protected_var)  # This will print: Changed by ChildA























# # class MyClass:
# #     class_var = 0  # Class variable

# #     def __init__(self, name):
# #         MyClass.class_var+=1
# #         self._myprivate_var
# #         self.name = name  # Instance variable
# #         self.instance_var = "I am an instance variable"  # Instance variable

# #     def show(self):
        
# #         return f"Name: {self.name}, Instance Var: {self.instance_var}, Class Var: {MyClass.class_var}"

# # class B(MyClass):
# #     def __init__(self,name):
# #         super().__init__(name)

# # class C(MyClass):
# #     def __init__(self,name):
# #         super().__init__(name)

# # # Creating instances
# # # MyClass.class_var = "MyClass.class_var"
# # obj1 = MyClass("Object 1")
# # obj2 = B("Object 2")
# # obj2 = C("Object 3")
# # print(MyClass.class_var)




# class MyNewClass:
#     def __init__(self):
#         self._protected_var = "hello"
#         self.__private_var = "ss"
#     def get_private_var(self):
#         return self.__private_var



# class MySecondClass(MyNewClass):
#     def __init__(self):
#         self._protected_var = "World"
#         print(self.__private_var)





# v = MyNewClass()

# print(v.get_private_var())







from abc import ABC, abstractmethod

# Abstract class with abstract and concrete methods
class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass
    
    def stop_engine(self):
        print("Engine stopped")

# Concrete class implementing all abstract methods
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

# Concrete class must implement the abstract method to be instantiable
car = Car()
car.start_engine()  # Output: Car engine started
car.stop_engine()   # Output: Engine stopped

# If we don't implement the abstract method, we get an error:
class Bike(Vehicle):
    pass

# Attempting to instantiate 'Bike' will result in a TypeError
# bike = Bike()  # Raises TypeError: Can't instantiate abstract class Bike with abstract method start_engine
