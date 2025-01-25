def main():
    lines=int(input("Enter the number of lines: "))
    for i in range(1,lines+1):
        for j in range(i):
            print('*',end='')
        print("\n")
    
main()