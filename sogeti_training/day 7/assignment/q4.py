from abc import ABC,abstractmethod
class father:
    @abstractmethod
    def profession(self):
        pass
    def introduse(self):
        print("i am father")
        self.profession()

class engineer(father):
    def profession(self):
        print("I am engineer")
    
class docter(father):
    def profession(self):
        print("I am docter")

e=engineer()
e.introduse()
d=docter()
d.introduse()