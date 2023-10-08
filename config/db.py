from urllib.parse import quote_plus
from pymongo import MongoClient

# Encode the username and password
username = "anushka"
password = "Anu@12345"
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

# MongoDB Atlas connection string with encoded username and password
uri = f"mongodb://{encoded_username}:{encoded_password}@ac-2y3cnu2-shard-00-00.medfjfh.mongodb.net:27017,ac-2y3cnu2-shard-00-01.medfjfh.mongodb.net:27017,ac-2y3cnu2-shard-00-02.medfjfh.mongodb.net:27017/?ssl=true&replicaSet=atlas-6rzj10-shard-0&authSource=admin&retryWrites=true&w=majority"

# Create the MongoDB client
conn = MongoClient(uri)

# Access the database (assuming you have a database named 'mydatabase')
db = conn['rentmaster']
