from pydantic import BaseModel
from bson import ObjectId
from typing import List, Union


class User(BaseModel):
    name: str
    email: str
    user_type: str = ("customer", "worker")
    job_types: Union[None, list]
    password: str


class Worker(User):
    job: str
    skills: List[str]
    descriptions: str
    work_type: str
    rating: float


class LoginData(BaseModel):
    email: str
    password: str
