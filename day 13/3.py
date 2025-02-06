class StuTable:
    def __init__(self,id,name,standard):
        self.id=id
        self.name=name
        self.standard=standard
    
class MarkTable:
    def __init__(self,id,mark):
        self.id=id
        self.mark=mark
    
class SqlOperation:
    def __init__(self,student,marks):
        self.student=student
        self.marks=marks
    
    def joinTable(self):
        mark_ids=[mark.id for mark in self.marks]
        stutable_list=[student for student in self.student if student.id in mark_ids]
        return stutable_list

    def selectByStandard(self,standard):
        return [student for student in self.student if student.standard==standard]
    

s1 = StuTable(1,"John",3)
s2= StuTable(2,"Jack",3)
s3= StuTable(3,"Jerry",4)
s4 = StuTable(4,"Tim",5)
m1 = MarkTable(1,99)
m2 = MarkTable(2,99)
m3 = MarkTable(2,80)
sql1 = SqlOperation ([s1,s2,s3,s4], [m1, m2, m3 ])
result = sql1.joinTable()
for i in result:
    print(i.id, i.name)