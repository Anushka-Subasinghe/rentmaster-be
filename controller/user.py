from typing import List, Dict
from models.user import User
from schemas.serialize import serializeDict, serializeList
from config.db import db
from bson import ObjectId

def create(user: User):
    print("<===== Create User =====>")
    inserted_result = db.user.insert_one(dict(user))
    inserted_user = db.user.find_one({"_id": inserted_result.inserted_id})
    return serializeDict(inserted_user)
    
def getAll():
    print("<===== Get All User =====>")
    return serializeList(db.user.find())


def getOne(id):
    print("<===== getLastOne =====>")
    res = serializeDict(db.user.find_one({"_id": ObjectId(id)}))
    print(res)
    return res

def update(id, user: User):
    db.user.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })
    inserted_doc = db.user.find_one({"_id": ObjectId(id)})
    return serializeDict(inserted_doc)

def delete(id: str):
    print("<===== delete User =====>", id)
    result = db.user.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"status_code": 200, "detail": "User Deleted" }