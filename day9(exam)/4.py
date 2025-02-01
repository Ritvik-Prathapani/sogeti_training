class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    
    def student_details(self):
        return f"name is {self.name}\nroll number is {self.rollno}"
    
newstudent=student('ritvik','21H51A05C4')
print(newstudent.student_details())