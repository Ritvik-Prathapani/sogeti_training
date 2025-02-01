from abc import ABC,abstractmethod

class Ivehicle(ABC):
    @abstractmethod
    def startengine(self):
        pass
    @abstractmethod
    def stopengine(self):
        pass

class car(Ivehicle):
    def startengine(self):
        print("car engine started")
    def stopengine(self):
        print("car engine stopped")

class bike(Ivehicle):
    def startengine(self):
        print("bike engine started")
    def stopengine(self):
        print("bike engine stopped")

class truck(Ivehicle):
    def startengine(self):
        print("truck engine started")
    def stopengine(self):
        print("truck engine stopped")

c=car()
c.startengine()
c.stopengine()


b=bike()
b.startengine()
b.stopengine()


t=truck()
t.startengine()
t.stopengine()