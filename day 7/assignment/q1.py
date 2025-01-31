from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        print("bark")

class cat(animal):
    def sound(self):
        print("meow")

d=dog()
d.sound()
c=cat()
c.sound()  
