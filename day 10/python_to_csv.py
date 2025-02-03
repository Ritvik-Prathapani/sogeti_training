import csv
import random
import os  

class Employee:
    def __init__(self, name, age, email):
        self.empid = random.randint(1, 1000)  
        self.name = name
        self.age = age
        self.email = email

    def get_details(self):
        return {
            'empid': self.empid,
            'name': self.name,
            'age': self.age,
            'email': self.email
        }

class EmpDetails:
    def __init__(self):
        self.emp_list = []

    def add_employee(self, employee):
        self.emp_list.append(employee)

    def get_all_employees(self):
        return [emp.get_details() for emp in self.emp_list]

class ToCSV:
    csv_file = "employee.csv"
    csv_columns = ['empid', 'name', 'age', 'email']

    @staticmethod
    def save_to_csv(employees):
        file_exists = os.path.exists(ToCSV.csv_file)  
        try:
            with open(ToCSV.csv_file, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=ToCSV.csv_columns)
                
                if not file_exists:  # Write header only if file is new
                    writer.writeheader()

                for emp in employees:
                    writer.writerow(emp)
            print("Data successfully saved to employee.csv")
        except IOError:
            print("IO error: Unable to write to file",IOError)

# Main Execution
if __name__ == "__main__":
    emp_details = EmpDetails()

    n = int(input("Enter the number of employees: "))
    for _ in range(n):
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        email = input("Enter Email: ")
        employee = Employee(name, age, email)
        emp_details.add_employee(employee)

    # Save to CSV
    ToCSV.save_to_csv(emp_details.get_all_employees())
