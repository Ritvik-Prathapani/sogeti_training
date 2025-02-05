import pandas as pd
df = pd.read_csv("sogeti_training\day 12\customers-1000.csv")
print(df.head())
# print(df.info())
# print(df.describe())
# print(df['Index'].mean())
# print(df[df["First Name"]=="Andrew"])

jsonfile=df.to_json('name.json',orient='records',lines=True,indent=1)
print(jsonfile)
