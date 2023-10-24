from pydantic import BaseModel
from bson import ObjectId
from typing import List, Union


class User(BaseModel):
    name: str
    email: str
    user_type: str = ("customer", "worker")
    job_types: Union[None, list]
    password: str


class UpdateUser(BaseModel):
    id: str
    user_type: str
    username: str
    email: str
    phone: str
    rating: float   


class Worker(User):
    job: str
    skills: List[str]
    descriptions: str
    work_type: str
    rating: float


class LoginData(BaseModel):
    email: str
    password: str

class JobType(BaseModel):
    JobType: str    
