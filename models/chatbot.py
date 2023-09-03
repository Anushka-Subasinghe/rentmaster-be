from pydantic import BaseModel
from bson import ObjectId
from typing import List 

class Chatbot(BaseModel):
    msg: str
    isUser: bool
    _id: str
    