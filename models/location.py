from pydantic import BaseModel
from bson import ObjectId

class Location(BaseModel):
    date: str
    day: str
    time: str
    reason: str
    location: str
    _id: str
    
