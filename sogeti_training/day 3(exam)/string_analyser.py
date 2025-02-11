def main():
    mystr=input("Enter the string to analize it: ")
    vowels=0
    consonents=0
    digits=0
    special_char=0
    vowels_options=['a','e','i','o','u']
    for i in mystr:
        if i in vowels_options:
            vowels+=1
        elif i.isalpha():
            consonents+=1
    for i in mystr:
        if i.isdigit():
            digits+=1
        elif not i.isalnum():
            special_char+=1
    revstr=mystr[::-1]
    print(f"the reverse of the string is {revstr}")
    print(f"the number of vowels in the string is {vowels}")
    print(f"the number of consonents in the string is {consonents}")
    print(f"the number of digits in the string is {digits}")
    print(f"the number of special characters in the string is {special_char}")  

main()