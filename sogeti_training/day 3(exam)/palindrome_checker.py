def main():
    str=input("Enter string to check whether palindrome or not: ")
    str_length=len(str)
    lastpointer=str_length-1
    startpointer=0
    is_palindrome=False
    while(startpointer<lastpointer):
        if str[startpointer]==str[lastpointer]:
            startpointer+=1
            lastpointer-=1
            is_palindrome=True
        else:
            startpointer+=1
            lastpointer-=1  
            is_palindrome=False
        
    if is_palindrome:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")

main()