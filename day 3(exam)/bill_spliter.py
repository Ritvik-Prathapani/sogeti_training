def main():
    print("Biill Spliter")
    people=int(input("Enter the number of people: "))
    bill=float(input("Enter the total bill: "))
    tip=float(input("enter the tip percentaage: "))
    total=bill+(bill*tip/100)
    print(f"Total bill with tip is {total}")
    per_person=total/people
    print(f"Each person should pay {per_person}")

main()