import json
from fastapi import HTTPException, status
from typing import List, Dict
from models.advertisement import Advertisement
from schemas.serialize import serializeDict, serializeList
from config.db import db
from bson import ObjectId

def post_advertisement(advertisement: Advertisement):
    print("<===== Create Advertisement =====>")
    user = db.users.find_one({"email": advertisement.email})
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )

    # Create the job document
    advertisement = {
        "job_type": advertisement.job_type,
        "date": advertisement.date,
        "time": advertisement.time,
        "email": advertisement.email,
        "status": advertisement.status,
        "customer_name": user["username"]
    }

    # Insert the job into the database
    inserted_result = db.advertisements.insert_one(advertisement)
    inserted_advertisement = db.advertisements.find_one({"_id": inserted_result.inserted_id})

    return serializeDict(inserted_advertisement)
    
def getAll():
    print("<===== Get All Advertisement =====>")
    return serializeList(db.advertisement.find())

def getAdvertisementsByCustomer(email: str):
    print("<===== get Customer Advertisements =====>")

    # Query the database to find all advertisements with the specified email
    advertisements = db.advertisements.find({"email": email})

    # Convert the MongoDB cursor to a list of dictionaries excluding _id
    advertisements_list = []
    for ad in advertisements:
        ad['_id'] = str(ad['_id'])
        advertisements_list.append(ad)

    if advertisements_list:
        return json.dumps({"advertisements": advertisements_list})
    else:
        return json.dumps({"advertisements": []})
    
def getAdvertisementsByJobType(job_types: list):
    print("<===== get Job Type Advertisements =====>")

    # Query the database to find all advertisements with the specified job types
    advertisements = db.advertisements.find({"job_type": {"$in": job_types}})

    # Convert the MongoDB cursor to a list of dictionaries excluding _id
    advertisements_list = []
    for ad in advertisements:
        ad['_id'] = str(ad['_id'])
        advertisements_list.append(ad)

    print(advertisements_list)    

    if advertisements_list:
        return json.dumps({"advertisements": advertisements_list})
    else:
        return json.dumps({"advertisements": []})   

def update(id, advertisement: Advertisement):
    print("<===== update Advertisement =====>")
    db.advertisement.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(advertisement)
    })
    inserted_doc = db.advertisement.find_one({"_id": ObjectId(id)})
    return serializeDict(inserted_doc)

def delete(id: str):
    print("<===== delete Advertisement =====>", id)
    result = db.advertisements.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Advertisement not found")
    return {"status_code": 200, "detail": "Advertisement Deleted" }
