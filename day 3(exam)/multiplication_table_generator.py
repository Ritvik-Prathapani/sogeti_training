def main():
    number=int(input("Enter a number to display it multiplication table: "))
    for i in range(1,11):
        print(f"{number} * {i} = {int(number)*i}")  
main()