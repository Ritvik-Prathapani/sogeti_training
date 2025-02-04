import pymongo

# MongoDB Atlas connection string
client = pymongo.MongoClient("mongodb+srv://ritvik:3613@cluster0.qzdk4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Select a database
db = client["temp"]

# Access a collection
collection = db["cluster0"]

# Example: Insert a document
collection.insert_one({'temp':'hello'})

# Example: Find documents
documents = collection.find()   
for doc in documents:
    print(doc)

# Close the connection
client.close()
