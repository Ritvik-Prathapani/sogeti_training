from abc import ABC,abstractmethod

class myclass(ABC):
    @abstractmethod
    def display(self):
        pass.
    def mystatement(self):
        print("hello")

class newclass(myclass):
    def display(self):
        print("display")
    
c1=newclass()
c1.display()
c1.mystatement()