
from abc import ABC , abstractmethod



class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
        
    @abstractmethod
    def turn_off(self):
        pass

class Radio(Switchable):
    def turn_on(self):
        print(f"turned on {self.__class__.__name__}")
    def turn_off(self):
        print(f"turned off {self.__class__.__name__}")


class LightBulb(Switchable):
    def turn_on(self):
        print(f"turned on {self.__class__.__name__}")
    def turn_off(self):
        print(f"turned off {self.__class__.__name__}")



class LightSwitch:
    def __init__(self,device:Switchable):
        self.device = device
    
    def operate(self,on):
        if on:
            self.device.turn_on()
        else:
            self.device.turn_off()


LightSwitch(LightBulb()).operate(True)
LightSwitch(Radio()).operate(True)
LightSwitch(LightBulb()).operate(on=False)
LightSwitch(Radio()).operate(on=False)
