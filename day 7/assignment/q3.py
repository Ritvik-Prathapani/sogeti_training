from abc import ABC,abstractmethod
import math

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth


class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi * self.radius**2

r=rectangle(10,20)
c=circle(2)

print(f"the area of the circle is {c.area()}")
print(f"the area of ractangle is {r.area()}")

