from pydantic import BaseModel
from bson import ObjectId


class Weather(BaseModel):
    temp: float
    windspeed: float
    humidity: float
    rain_sum: float
    latitude: float
    longitude: float
    work_type: int
    
