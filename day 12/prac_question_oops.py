class StuTable:
  # Define all the variables and methods of StuTable class here
    def __init__(self,id,name,standard):
        self.id= id
        self.name= name
        self.standard= standard
  
class MarkTable:
  # Define all the variables and methods of MarkTable class here
    def __init__(self,id,mark):
        self.id= id
        self.mark= mark

class SqlOperation:
  # Define all the variables and methods of SqlOperation class here
    def __init__(self,students,marks):
        self.students= students
        self.marks= marks

    def joinTable(self):
        marked_ids=set()
        #marked_ids={marks.id for marks in self.marks}
        for i in self.marks:
            marked_ids.add(i.id)
        # return [student for student in self.students if student.id in marked_ids]
        ans_list=[]
        for i in self.students:
            if i.id in marked_ids:
                ans_list.append(i)
        return ans_list
            

    def selectByStandard(self,standard):
        # return [student.name for student in self.students if student.standard==sta]
        anslist=[]
        for i in self.students:
            if i.standard==standard:
              anslist.append(i)
        return anslist



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
    # print(i.id,i.standard)