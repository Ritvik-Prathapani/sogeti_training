from abc import ABC,abstractmethod

class person(ABC):
    @abstractmethod
    def get_name(self):
        pass
    
class employee(ABC):
    @abstractmethod
    def get_salary(self):
        pass

class manager(person,employee):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_name(self):
        return self.name
    def get_salary(self):
        return self.salary

m=manager("tom",2000)
print(f"manager name:{m.get_name()}")
print(f"manager salary {m.get_salary()}")
