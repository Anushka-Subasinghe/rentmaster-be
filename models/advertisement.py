from pydantic import BaseModel
from bson import ObjectId

class Advertisement(BaseModel):
    f_name: str
    l_name: str
    email: str
    mobile: str
    district: str
    city: str
    address: str
    description: str
    time_of_service: str
    type: str
    file: str
    _id: str
    
