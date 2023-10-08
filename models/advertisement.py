from pydantic import BaseModel
from bson import ObjectId

class Advertisement(BaseModel):
    email: str
    date: str
    time: str
    job_type: str
    status: str
    
