class person:
    def __init__(self,name):
        self.name=name
    
class employee(person):
    def __init__(self,name,employeeid):
        super().__init__(name)
        employeeid=employeeid
    
class manager(employee):
    def __init__(self,name,empid,department):
        super().__init__(name,empid)
        self.department=department
    def approve_leave(self):
        return f"{self.name} is approving leave for the {self.department} department."

manage=manager("tom",1233,"it")
print(manage.approve_leave())