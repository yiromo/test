import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://admin:voxTaPqIcCC4QvwS@fastapi.3wiu5mv.mongodb.net/?retryWrites=true&w=majority&appName=FastAPI"
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


class Disease(BaseModel):
    name: str
    description: str

app = FastAPI()

diseases = []

@app.get("/")
def main_function():
    return {"message": "test"}

@app.get("/diseases", response_model=list[Disease])
def get_diseases():
    return diseases

@app.post("/diseseas")
def new_disease(disease: Disease = Body(...)):
    diseases.append(disease)
    return disease



if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")