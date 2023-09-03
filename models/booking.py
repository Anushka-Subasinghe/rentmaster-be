from pydantic import BaseModel
from bson import ObjectId
from models.user import Worker
from models.user import User


class Booking(BaseModel):
    worker: Worker
    customer: User
    start_date: str
    end_date: str
    start_time: str
    end_time: str
    district: str
    city: str
    address: str
    location: str
    description: str
    job: str # new added
    _id: str
    
