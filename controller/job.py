from fastapi import HTTPException
from typing import List, Dict
from models.job import Job
from schemas.serialize import serializeDict, serializeList
from config.db import db
from bson import ObjectId

def create(job: Job):
    print("<===== Create Job =====>")
    inserted_result = db.job.insert_one(dict(job))
    jnsert_Job = db.job.find_one({"_id": inserted_result.inserted_id})
    return serializeDict(jnsert_Job)
    
def getAll():
    print("<===== Get All Job =====>")
    return serializeList(db.job.find())

def getOne(id):
    print("<===== getLastOne Job =====>")
    res = serializeDict(db.job.find_one({"_id": ObjectId(id)}))
    if res:
        return res
    raise HTTPException(status_code=404, detail="Job not found")

def update(id, job: Job):
    print("<===== update Job =====>")
    db.job.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(job)
    })
    inserted_doc = db.job.find_one({"_id": ObjectId(id)})
    return serializeDict(inserted_doc)

def delete(id: str):
    print("<===== delete Job =====>")
    result = db.job.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"status_code": 200, "detail": "Job Deleted" }
