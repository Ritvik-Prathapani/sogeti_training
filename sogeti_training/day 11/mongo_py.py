import pymongo
import pandas as pd
# MongoDB Atlas connection string
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select a database
db = client["practise"]

# Access a collection
collection = db["temp1"]

df=pd.read_csv("sogeti_training\day 12\customers-1000.csv")
# Example: Insert a document
data=df.to_dict(orient='records')
collection.insert_many(data)

# Example: Find documents
documents = collection.find() 
for doc in documents:
    print(doc)

# Close the connection
client.close()
