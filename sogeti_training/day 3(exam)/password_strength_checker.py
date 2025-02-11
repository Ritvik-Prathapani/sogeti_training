def main():
    print("this is a password strength checker")
    password = input("Enter a password: ")
    if(len(password) < 8):
        print("Password is weak")
    check=0 #each check has 1 point uppercase,lowercase,digits,specialcharecter
    vowels=['a','e','i','o','u']
    found_vowel=False
    found_isalnum=False
    found_digit=False
    found_special=False
    for i in password:
        if i in vowels and found_vowel==False:
            check+=1
            found_vowel=True
        elif i.isalnum() and found_isalnum==False:
            check+=1
            found_isalnum=True
        elif i.isdigit() and found_digit==False:
            check+=1
            found_digit=True
        elif i not in vowels and not i.isalnum() and not i.isdigit() and found_special==False:
            check+=1
            found_special=True
    if check == 4:
        print("Password is strong")
    else:    
        print("password is weak")
    print(check)
main()