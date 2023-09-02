from pydantic import BaseModel
from bson import ObjectId

class Worker(BaseModel):
    name: str 
    mobile: str

class Customer(BaseModel):
    name: str 
    mobile: str    
    
class Booking(BaseModel):
    worker: Worker
    customer: Customer
    start_date: str
    end_date: str
    start_time: str
    end_time: str
    district: str
    city: str
    address: str
    location: str
    description: str
    _id: str
    
