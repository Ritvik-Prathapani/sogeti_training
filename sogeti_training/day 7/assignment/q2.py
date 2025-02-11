from abc import ABC,abstractmethod
class vehicle(ABC):
    def __init__(self,brand):
        self.brand=brand
    @abstractmethod
    def max_speed(self):
        pass

class car(vehicle):
    def max_speed(self):
        return 200
    
class bike(vehicle):
    def max_speed(self):
        return 150

v=car("audi")
b=bike("ktm")
print(f"{v.brand} is goint in {v.max_speed()}")
print(f"{b.brand} is goint in {b.max_speed()}")
    
