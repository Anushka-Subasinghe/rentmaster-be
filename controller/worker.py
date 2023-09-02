from fastapi import HTTPException
from typing import List, Dict
from models.user import Worker
from schemas.serialize import serializeDict, serializeList
from config.db import conn, db
from bson import ObjectId

def create(worker: Worker):
    print("<===== Create Worker =====>")
    inserted_result = db.worker.insert_one(dict(worker))
    insert_worker = db.worker.find_one({"_id": inserted_result.inserted_id})
    return serializeDict(insert_worker)
    
def getAll():
    print("<===== Get All Worker =====>")
    return serializeList(db.worker.find())

def getOne(id):
    print("<===== getLastOne Worker =====>")
    res = serializeDict(db.worker.find_one({"_id": ObjectId(id)}))
    if res:
        return res
    raise HTTPException(status_code=404, detail="Worker not found")

def update(id, worker: Worker):
    print("<===== update Worker =====>")
    db.worker.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(worker)
    })
    inserted_doc = db.worker.find_one({"_id": ObjectId(id)})
    return serializeDict(inserted_doc)

def delete(id: str):
    print("<===== delete Worker =====>")
    result = db.worker.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Worker not found")
    return {"status_code": 200, "detail": "Worker Deleted" }
