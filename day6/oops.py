#understanding static variables
class car:
    wheels=4
    def __init__(self,brand,car):
        self.brand=brand
        self.car=car
#understanding static methods
class maths:
    number=10
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def mul(a,b):
        return a*b
    @staticmethod  
    def div(a,b):
        return a/b

#understanding polymorphism
class maths2:
    def add(self,*args):
        return sum(args)
    def sub(self,a,b=0,c=0):
        return a-b-c
    def mul(self,a,b=1,c=1):
        return a*b*c
    def display(self):
        print("this is the parent class")
class newmath(maths2):
    def display(self):
        print("this is the child class")


#kwargs
class example:
    def __init__(self,**kwargs):
        self.kwargs=kwargs
        for k,v in kwargs.items():
            print(f'{k}={v}')
    def display(self):
        print(self.kwargs)

#multiple inheritance
class Lion:
    def roar(self):
        print("roar")

class Dog:
    def roar(self):
        print("bark")

class animal(Lion,Dog):
    def sound(self):
        print("sound")

obj=animal()
obj.roar()
obj.sound()