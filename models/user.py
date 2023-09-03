from pydantic import BaseModel
from bson import ObjectId
from typing import List 

class User(BaseModel):
    name: str
    dob: str
    mobile: str
    email: str
    user_type: str
    _id: str
    firebase_id: str
    
class Worker(User):
    job: str
    skills: List[str]
    descriptions: str
    work_type: str
    rating: float