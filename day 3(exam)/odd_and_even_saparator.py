def main():
    even=[]
    odd=[]
    numlist=list(map(int,input("enter the list of numbers: ").split()))
    for i in numlist:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print("even list is ",even)
    print("odd list is ",odd)

main()