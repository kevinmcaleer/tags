from pymongo import MongoClient

# Replace 'mongodb://localhost:27017/' with your MongoDB connection URI as needed.
client = MongoClient("mongodb://192.168.2.2:27017/")

# Choose the database name you want to use. If it doesn't exist, it will be created.
db = client["my_database"]

# Choose the collection you want to store data in. If it doesn't exist, it will be created.
collection = db["my_collection"]

def insert_data():
    # Here is the data you want to store. It can be any valid Python dictionary.
    document = {
        "name": "Alice",
        "age": 29,
        "hobbies": ["reading", "cycling", "coding"]
    }
    
    # Insert the document into the collection.
    insert_result = collection.insert_one(document)
    
    # Confirm the insertion by printing the inserted ID.
    print("Document inserted with _id:", insert_result.inserted_id)

def read_data():
    # Find the first document in the collection.
    document = collection.find_one()
    
    # Print the document.
    print(document)                        



if __name__ == "__main__":
    # insert_data()

    read_data()
