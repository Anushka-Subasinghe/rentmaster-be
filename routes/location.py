from fastapi import APIRouter
from controller.location import create, getOne, getAll, update
from models.location import Location

location = APIRouter()

@location.post('/location')
async def create(location: Location):
    res = create(location)
    print("res : ", res)
    return res

@location.get('/location/{id}')
async def get_by_id(id: str):
    location = getOne(id)
    if location:
        return location
    return {"message": "Location not found"}

@location.put('/location/{id}')
async def update_by_id(id: str, location: Location):
    location_db = update(id, location)
    if location_db:
        return location_db
    return {"message": "Location not found"}

@location.get('/location')
async def get_all():
    locations = getAll()
    return locations