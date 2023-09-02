from fastapi import HTTPException
from typing import List, Dict
from models.advertisement import Advertisement
from schemas.serialize import serializeDict, serializeList
from config.db import db
from bson import ObjectId

def create(advertisement: Advertisement):
    print("<===== Create Advertisement =====>")
    inserted_result = db.advertisement.insert_one(dict(advertisement))
    insert_advertisement = db.advertisement.find_one({"_id": inserted_result.inserted_id})
    return serializeDict(insert_advertisement)
    
def getAll():
    print("<===== Get All Advertisement =====>")
    return serializeList(db.advertisement.find())

def getOne(id):
    print("<===== getLastOne Advertisement =====>")
    res = serializeDict(db.advertisement.find_one({"_id": ObjectId(id)}))
    if res:
        return res
    raise HTTPException(status_code=404, detail="Advertisement not found")

def update(id, advertisement: Advertisement):
    print("<===== update Advertisement =====>")
    db.advertisement.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(advertisement)
    })
    inserted_doc = db.advertisement.find_one({"_id": ObjectId(id)})
    return serializeDict(inserted_doc)

def delete(id: str):
    print("<===== delete Advertisement =====>", id)
    result = db.advertisement.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    return {"status_code": 200, "detail": "Advertisement Deleted" }
