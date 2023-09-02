from typing import List, Dict
from models.location import Location
from schemas.serialize import serializeDict, serializeList
from config.db import conn
from bson import ObjectId

def create(location: Location):
    print("<===== Create Location =====>")
    conn.nest.location.insert_one(dict(location))
    
def getAll():
    print("<===== Get All Location =====>")
    return serializeList(conn.nest.location.find())

def getOne(id):
    print("<===== getOne =====>")
    res = serializeDict(conn.nest.location.find_one({"_id": ObjectId(id)}))
    print(res)
    return res
