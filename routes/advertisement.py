from fastapi import APIRouter
from controller.advertisement import create, getOne, getAll, update, delete
from models.advertisement import Advertisement

advertisement = APIRouter()

@advertisement.post('/advertisement')
async def create_advertisement(advertisement: Advertisement):
    return create(advertisement)

@advertisement.get('/advertisement/{advertisement_id}')
async def get_advertisement_by_id(advertisement_id: str):
    return getOne(advertisement_id)

@advertisement.delete('/advertisement/{advertisement_id}')
async def delete_advertisement(advertisement_id: str):
    return delete(advertisement_id)

@advertisement.put('/advertisement/{advertisement_id}')
async def update_advertisement(advertisement_id: str, updated_advertisement: Advertisement):
    return update(advertisement_id, updated_advertisement)
    
@advertisement.get('/advertisements')
async def get_all_advertisements():
    return getAll()

