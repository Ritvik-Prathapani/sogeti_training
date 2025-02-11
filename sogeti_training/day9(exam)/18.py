from abc import ABC,abstractmethod
class Icalculator:
    @abstractmethod
    def add(self,num1,num2):
        pass
    def subtract(self,num1,num2):
        pass
    def multiply(self,num1,num2):
        pass
    def divide(self,num1,num2):
        pass

class basicCalculator(Icalculator):
    def add(self, num1, num2):
        print(f"the addition of the numbers is {num1+num2}")
    def subtract(self, num1, num2):
        print(f"the subtraction of the numbers is {num1-num2}")
    def multiply(self, num1, num2):
        print(f"the multiplication of the numbers is {num1*num2}")
    def divide(self, num1, num2):
        print(f"the divition of the numbers is {num1/num2:.2f}")

obj=basicCalculator()
obj.add(1,2)
obj.subtract(4,2)
obj.multiply(3,2)
obj.divide(4,2)