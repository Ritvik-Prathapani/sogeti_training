def main():
    number=int(input("Enter a number to calculate its factorial"))
    answer=1
    for i in range(1,number+1):
        answer*=i
    print(f"factorial is {answer}")
main()