from pydantic import BaseModel
from bson import ObjectId

class Forecast(BaseModel):
    weather: str
    temperature: float
    humidity: int
    windspeed: float   

class Advertisement(BaseModel):
    email: str
    date: str
    time: str
    job_type: str
    status: str
    latitude: float
    longitude: float
    forecast: Forecast
    work_type: int

class BidAdvertisement(BaseModel):
    id: str
    worker_name: str
    worker_id: str
    price: float

class CancelBid(BaseModel):
    id: str
    worker_id: str

class CancelJob(BaseModel):
    id: str               

class AcceptAdvertisement(BaseModel):
    id: str
    worker_name: str
    worker_id: str
    price: float
