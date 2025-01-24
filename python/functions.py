'''
#to find avg of 4 numbers
def get_input():
    num1=int(input("enter first number: "))
    num2=int(input("enter second number: "))
    num3=int(input("enter third number: "))
    num4=int(input("enter fourth number: "))
    return num1,num2,num3,num4
def get_avg(num1,num2,num3,num4):
    avg=(num1+num2+num3+num4)/4
    return avg
def main():
    print("enter 4 numbers: ")
    (num1,num2,num3,num4) = get_input()
    avg=get_avg(num1,num2,num3,num4)
    print("average of 4 numbers is: ",avg)

main()
'''

'''
#to find avg of n numbers
def get_avg(a):
    list_size=len(a)
    sum_of_list=0
    for i in a:
        sum_of_list+=i
    return sum_of_list/list_size
def main():
    a=[]
    n = int(input("enter the number of values: "))
    for i in range(n):
        val=int(input(f"enter the value {i+1}: "))
        a.append(val)
    avg=get_avg(a)
    print(f'avg value is: {avg}')
main()
'''
#to find greatest among 3 numbers
def get_input():
    a=int(input("enter first number: "))
    b=int(input("enter second number: "))
    c=int(input("enter third number: "))
    return a,b,c
def find_max(a,b,c):
    max=-1
    if(a>b and a>c):
        max=a
    elif(b>a and b>c):
        max=b
    else:
        max=c
    return max

def main():
    a,b,c=get_input()
    max_value=find_max(a,b,c)
    print(f"max value is: {max_value}")
main()
