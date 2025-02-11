import math
def is_prime(num):
    if num==1:
        return False
    if num==2:
        return True
    if num%2==0:
        return False
    i=3
    while i<=math.sqrt(num):
        if num%i==0:
            return False
        i+=2
    return True

def get_input():
    start=int(input("Enter the starting value"))
    end=int(input("Enter the ending value"))
    return start,end
def main():
    print("Enter numbers between which you want to find prime numbers")
    start_range,end_range=get_input()
    lst=[i for i in range(start_range,end_range) if is_prime(i)]
    for i in lst:
        print(i)
    
main()