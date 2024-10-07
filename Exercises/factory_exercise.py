
from abc import ABC
class Vehicle:
    def __init__(self,engine,wheels,color):
        self.engine = engine
        self.wheels = wheels
        self.color = color

    def __str__(self):
        return f"""( engine : {self.engine} wheels : {self.wheels} color : {self.color} )"""
    def move(self):
        pass






class Car(Vehicle):
    pass

class MotorCycle(Vehicle):
    pass

class SedanCar(Car):
    pass

class SUVCar(Car):
    pass

class VehicleFactory(ABC):
    def make_vehicle(self):
        pass


class SedanCarFactory(VehicleFactory):
    def make_vehicle(self):
        return SedanCar("V8",4,"Red")

class SUVCarFactory(VehicleFactory):
    def make_vehicle(self):
        return SUVCar("V10",4,"Black")

class MotorCycleFactory(VehicleFactory):
    def make_vehicle(self):
        return MotorCycle("Twin Cylinder",2,"Blue")




sedan = SedanCarFactory().make_vehicle()
suv = SUVCarFactory().make_vehicle()
motorcycle = MotorCycleFactory().make_vehicle()
print(sedan)
print(suv)
print(motorcycle)