from fastapi import HTTPException
from typing import List, Dict
from models.booking import Booking
from schemas.serialize import serializeDict, serializeList
from config.db import db
from bson import ObjectId

def create(booking: Booking):
    print("<===== Create Booking =====>")
    inserted_result = db.booking.insert_one(dict(booking))
    insert_booking = db.booking.find_one({"_id": inserted_result.inserted_id})
    return serializeDict(insert_booking)
    
def getAll():
    print("<===== Get All Booking =====>")
    return serializeList(db.booking.find())

def getOne(id):
    print("<===== getLastOne Booking =====>")
    res = serializeDict(db.booking.find_one({"_id": ObjectId(id)}))
    if res:
        return res
    raise HTTPException(status_code=404, detail="Booking not found")

def update(id, booking: Booking):
    print("<===== update Booking =====>")
    db.booking.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(booking)
    })
    inserted_doc = db.booking.find_one({"_id": ObjectId(id)})
    return serializeDict(inserted_doc)

def delete(id: str):
    print("<===== delete Booking =====>", id)
    result = db.booking.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"status_code": 200, "detail": "Booking Deleted" }
