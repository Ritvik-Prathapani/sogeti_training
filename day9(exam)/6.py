class vehicle:
    def display(self):
        print("this is a vehicle")

class car(vehicle):
    def display(self):
        super().display()
        print("car")

class bike(vehicle):
    def display(self):
        super().display()
        print("bike")

class electriccar(car):
    def display(self):
        super().display()
        print("electric car")
    

v=vehicle()
v.display

c=car()
c.display()

b=bike()
b.display()

ec=electriccar()
ec.display()