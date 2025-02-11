class car:
    def move(self):
        return f"the car is moving on wheels"

class airplane:
    def move(self):
        return f"the airplane is moving through the sky"

class flyingcar(car,airplane):
    def __init__(self):
        self.car=car()
        self.airplane=airplane()
    def move(self):
        return f"{self.car.move()} {self.airplane.move()}"

vehicle=flyingcar()
print(vehicle.move())