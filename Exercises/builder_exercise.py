
from abc import ABC,abstractmethod
class Vehicle:
    def __init__(self):
        self.engine = None
        self.wheels = None
        self.color = None

    def __str__(self):
        return f"""( engine : {self.engine} wheels : {self.wheels} color : {self.color} )"""
    def move(self):
        pass




class VehicleBuilder:
    def __init__(self,vehicle):
        self.vehicle = vehicle

    def set_engine(self, engine_name : str) -> 'VehicleBuilder':
        self.vehicle.engine = engine_name
        return self

    def set_wheels(self, wheels_number : int) -> 'VehicleBuilder':
        self.vehicle.wheels = wheels_number
        return self

    def set_color(self, color_type: str) -> 'VehicleBuilder':
        self.vehicle.color = color_type
        return self

    def build(self) -> Vehicle:
        return self.vehicle




class Car(Vehicle):
    def move(self):
        print(f"{self.__class__.__name__} is moving!")


class MotorCycle(Vehicle):
    def move(self):
        print(f"{self.__class__.__name__} is moving!")

class SedanCar(Car):
    def move(self):
        print(f"{self.__class__.__name__} is moving!")

class SUVCar(Car):
    def move(self):
        print(f"{self.__class__.__name__} is moving!")

class VehicleFactory(ABC):
    def make_vehicle(self):
        pass


class SedanCarFactory(VehicleFactory):
    def make_vehicle(self) -> Vehicle:
        return VehicleBuilder(SedanCar()).set_engine("V8").set_color("#000").set_wheels(4).build()


class SUVCarFactory(VehicleFactory):
    def make_vehicle(self) -> Vehicle:
        return VehicleBuilder(SUVCar()).set_engine("V6").set_color("#256").set_wheels(4).build()


class MotorCycleFactory(VehicleFactory):
    def make_vehicle(self) -> Vehicle:
        return VehicleBuilder(MotorCycle()).set_engine("Twin Cylinder").set_color("#200").set_wheels(2).build()





sedan = SedanCarFactory().make_vehicle()
suv = SUVCarFactory().make_vehicle()
motorcycle = MotorCycleFactory().make_vehicle()
print(sedan)
sedan.move()
print(suv)
suv.move()
print(motorcycle)
motorcycle.move()