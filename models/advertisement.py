from pydantic import BaseModel
from bson import ObjectId

class Advertisement(BaseModel):
    email: str
    date: str
    time: str
    job_type: str
    status: str
    latitude: float
    longitude: float
    forecast: str

class UpdateAdvertisement(BaseModel):
    id: str
    status: str
    worker_name: str
    worker_id: str    
    
