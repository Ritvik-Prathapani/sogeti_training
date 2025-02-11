#assuming that each subject is of 100 marks total is 500 marks

#this function is used to get percentage
def get_percentage(marks):
    percentage = (marks/500)*100
    return percentage

#this function is used to get grade
def get_grade(percent):
    grade = ''
    percentage = int(percent)
    if(percentage<35):
        grade = 'F'
    elif(percentage<=60):
        grade = 'C'
    elif (percentage<=80):
        grade = 'B'
    elif(percentage<=100):
        grade = 'A'
    return grade

#this is the main function
def main():
    print("This is a student grading system")
    student_name=input("Enter student name: ")
    total_marks=0
    for i in range(5):
        mark=int(input(f"Enter marks for subject {i+1}: "))
        total_marks+= mark
    percentage=get_percentage(total_marks)
    grade=get_grade(percentage)
    print(f"{student_name}")
    print(f"Total marks: {total_marks}")
    print(f"Percentage: {percentage}")
    print(f"Grade: {grade}")

main()#starts the code