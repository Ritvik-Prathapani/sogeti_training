def main():
    weight=float(input("Enter the weight in kgs"))
    height=float(input("Enter the height in meters"))
    bmi=height/(weight**2)
    print(f"bmi is {bmi}")
    if bmi<18:
        print("underweight")
    elif bmi<25:
        print("normal")
    elif bmi<30:
        print("obese")
    else:
        print("overweight")

main()