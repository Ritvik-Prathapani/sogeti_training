def main():
    str=input("enter a string: ").split()
    char_count={}
    for char in str:
        if char in char_count:
            char_count[char]+=1
        else:   
            char_count[char]=1
    for key,value in char_count.items():
        print(f"{key}: {value}")

