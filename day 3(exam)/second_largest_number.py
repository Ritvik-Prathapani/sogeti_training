def main():
    mylist=list(map(int,input("Enter all the values").split()))
    mylist.sort()
    list_size=len(mylist)
    print(f"the second largest number is {mylist[list_size-2]}")
main()