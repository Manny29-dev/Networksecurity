
try:
    from pymongo import MongoClient
    from pymongo.server_api import ServerApi
except ImportError as e:
    raise ImportError("pymongo is required to run this script. Install it with 'pip install pymongo'.") from e

uri = "mongodb+srv://imanuveljs:Admin123@cluster0.iul5knb.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)