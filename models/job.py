from pydantic import BaseModel
from bson import ObjectId

class Job(BaseModel):
    owner: str
    job_name: str
    location: str
    exprience: str
    f_name: str
    l_name: str
    email: str
    mobile: str
    district: str
    city: str
    address: str
    description: str
    skills: str
    type: str
    gender: str
    file: str
    _id: str
    
