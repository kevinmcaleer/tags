import yaml
from pymongo import MongoClient

def main():
    # Replace with your actual connection string if necessary
    client = MongoClient("mongodb://192.168.2.2:27017/")
    db = client["kevsrobots"]
    collection = db["youtube_videos"]

    # Path to your YAML file
    yaml_file_path = "/Users/Kev/Web/kevsrobots.com/web/_data/youtube.yml"

    # Load data from the YAML file
    with open(yaml_file_path, 'r') as f:
        data = yaml.safe_load(f)

    # `data` may be a single dict or a list of dicts depending on your YAML content.
    # If it's a single document, wrap it in a list for insertion.
    if isinstance(data, dict):
        data = [data]

    # Insert the documents into the MongoDB collection
    # `insert_many` requires a list of documents.
    result = collection.insert_many(data)

    print("Documents inserted with IDs:")
    for doc_id in result.inserted_ids:
        print(doc_id)

if __name__ == "__main__":
    main()
