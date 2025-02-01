import math
from abc import ABC,abstractmethod
class Ishape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class rectangle(Ishape):
    def calculate_area(self,l,b):
        print(f"the area of rectangle is {l*b}")
        
class circle(Ishape):
    def calculate_area(self,r):
        print(f"the area of circle is {math.pi*r**2:.2f}")
    
a1=rectangle()
a1.calculate_area(2,3)

a2=circle()
a2.calculate_area(2)