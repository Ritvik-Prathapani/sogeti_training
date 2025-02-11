class employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department

name=input("Enter employee name: ")
id=input("Enter employee id: ")
department=input("enter employee department: ")

emp1=employee(name=name,id=id,department=department)

print(f"employee name:{emp1.name}\nemployee id:{emp1.id}\nemployee department:{emp1.department}")


