testcases=int(input())
for _ in range(testcases):
    number_of_friends,number_of_queries=input().split()
    my_dict={}
    for _ in range(int(number_of_friends)):
        name,age,hobbies,chocolate=input().split()
        my_dict[name]=(age,hobbies,chocolate)

    for _ in range(int(number_of_queries)):
        query=input()
        age,hobbies,chocolate=my_dict[query]
        print(f"{age}, {hobbies}, {chocolate}")
