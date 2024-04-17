from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:voxTaPqIcCC4QvwS@fastapi.3wiu5mv.mongodb.net/?retryWrites=true&w=majority&appName=FastAPI")
db = client.fastapi
coll = db['bolesni']

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)