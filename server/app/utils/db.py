from pymongo import MongoClient
from app.config import MONGO_URI
from pymongo.server_api import ServerApi
""" Testing Mongo client connection """
# Create a new client and connect to the server
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

def test_connection():
# Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)    
