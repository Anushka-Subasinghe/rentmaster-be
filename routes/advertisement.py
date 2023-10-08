from typing import List
from fastapi import APIRouter, Path, Query
import urllib
from controller.advertisement import post_advertisement, getAdvertisementsByCustomer, getAdvertisementsByJobType, update, delete
from models.advertisement import Advertisement

advertisement = APIRouter()

@advertisement.post('/advertisement')
async def create_advertisement(advertisement: Advertisement):
    return post_advertisement(advertisement)

@advertisement.get('/advertisement/customer/{encoded_email}')
async def get_advertisement_by_customer(encoded_email: str = Path(...)):
    email = urllib.parse.unquote(encoded_email)
    return getAdvertisementsByCustomer(email)

@advertisement.get('/advertisement/jobType')
async def get_advertisement_by_job_types(job_types: List[str] = Query(...)):
    return getAdvertisementsByJobType(job_types)

@advertisement.delete('/advertisement/{advertisement_id}')
async def delete_advertisement(advertisement_id: str = Path(...)):
    return delete(advertisement_id)

@advertisement.put('/advertisement/{advertisement_id}')
async def update_advertisement(advertisement_id: str, updated_advertisement: Advertisement):
    return update(advertisement_id, updated_advertisement)
    
# @advertisement.get('/advertisements')
# async def get_all_advertisements():
#     return getAll()

