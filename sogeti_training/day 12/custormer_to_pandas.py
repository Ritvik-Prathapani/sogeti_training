import pandas as pd
# data=[]
# n=int(input("enter the number of records: "))
# for i in range(n):
#     name=input("enter name: ")
#     age=input("enter age: ")
#     data.append({"Name":name,"Age":age,"Index":i+1})

# df=pd.DataFrame(data).set_index("Index")
# df_sorted=df.sort_values(by='Index')
# # print(df_sorted)
# # print(df)
# csvfile=df_sorted.to_csv("customerinput.csv")

df2=pd.read_csv("customerinput.csv")
print(df2.head())