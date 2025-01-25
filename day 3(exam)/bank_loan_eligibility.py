def get_input():
    salary=int(input("Enter salary: "))
    age=int(input("Enter age: "))
    credit_score=int(input("Enter credit_score: "))
    return salary,age,credit_score
def main():
    salary,age,credit_score=get_input()
    if(salary>25000 and age>21 and credit_score>600):
        print("Eligible for loan")
    if(salary<25000):
        print("Not eligible for loan as low salary")
    if(age<21):
        print("Not eligible for loan as age is less than 21")
    if(credit_score<600):
        print("Not eligible for loan as credit score is less than 600")    

main()