import pandas as pd
# data = {
#     'Region': ['North', 'North', 'South', 'South', 'East', 'East'],
#     'State': ['Delhi', 'Punjab', 'Tamil Nadu', 'Karnataka', 'TG', 'Odisha'],
#     'Year': [2021, 2021, 2021, 2021, 2021, 2021],
#     'Sales': [750000, 820000, 690000, 720000, 670000, 710000],
#     'Profit': [95000, 102000, 85000, 91000,77000,88000]
# }
# df=pd.DataFrame(data)
# df.set_index(['Region','Year','State'],inplace=True)
# print(df)
# print(df.loc[('South','Tamil Nadu',2021),'Sales'])
# df_sales=pd.DataFrame({'State':['Delhi','Tamil Nadu','West Bengal'],'Sales':[12345,12321,12211]})
# df_profit=pd.DataFrame({'State':['Delhi','Tamil Nadu','West Bengal'],'Sales':[0,0,0]})
# df_merged=pd.merge(df_sales,df_profit,on='State',how='right')
# print(df_merged)

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data,index=['a','b','c'])

# Using .loc[] to select rows by label
row_by_label = df.loc['b']  # Selects the row with index label 1 (Bob's data)
 
# Using .iloc[] to select rows by position
row_by_position = df.iloc[1]  # Selects the second row (Bob's data)

print("Row by label:\n", row_by_label)
print("Row by position:\n", row_by_position)