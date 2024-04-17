from fastapi import APIRouter
from models.models import Disease
from config.database import coll
from schemas.schemas import list_diseases
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_diseases():
    diseases = list_diseases(coll.find())
    return diseases

@router.post("/")
async def new_disease(disease: Disease):
    coll.insert_one(dict(disease))

@router.put("/{id}")
async def update_disease(id: str, disease: Disease):
    coll.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(disease)})

@router.delete("/{id}")
async def delete_disease(id: str):
    coll.find_one_and_delete({"_id": ObjectId(id)})