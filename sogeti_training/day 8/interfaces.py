from abc import ABC,abstractmethod

class employee(ABC):
    @abstractmethod
    def work(self):
        pass
    def salary(self):
        pass

class manager(employee):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def work(self):
        return f"{self.name} is managing the team"
    
    def get_salary(self):   
        return self.salary
    
class devloper(employee):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def work(self):
        return f"{self.name} is writing code"
    
    def get_salary(self):
        return self.salary


class intern(employee):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def work(self):
        return f"{self.name} is learning"
    
    def get_salary(self):
        return self.salary

class department:
    def __init__(self,name):
        self.name=name
        self.employees=[]
    
    def hire(self,employee):
        self.employees.append(employee)
        print(f"{employee.name} has been added")

    def fire(self,employee):
        self.employees.remove(employee)
        print(f"{employee.name} has been fired")
    
    def total_salary(self):
        return sum(employee.salary() for employee in self.employees)

    def show_employee_details(self):
        print(f"employees in the {self.name} department")
        for employee in self.employees:
            print(f"name: {employee.name} salary: {employee.get_salary()} work: {employee.work()}")
    
manager=manager("alive",8000)
dept=department('it')
dept.hire(manager)

dept.show_employee_details()

    