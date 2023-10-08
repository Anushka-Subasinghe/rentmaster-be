from typing import List
from fastapi import APIRouter, Path, Query
import urllib
from controller.advertisement import post_advertisement, getAdvertisementsByCustomer, getAdvertisementsByJobType, update_advertisement, delete_advertisement
from models.advertisement import Advertisement, UpdateAdvertisement

advertisement = APIRouter()

@advertisement.post('/advertisement')
async def create(advertisement: Advertisement):
    return post_advertisement(advertisement)

@advertisement.get('/advertisement/customer/{encoded_email}')
async def get_advertisement_by_customer(encoded_email: str = Path(...)):
    email = urllib.parse.unquote(encoded_email)
    return getAdvertisementsByCustomer(email)

@advertisement.get('/advertisement/jobType')
async def get_advertisement_by_job_types(job_types: List[str] = Query(...)):
    return getAdvertisementsByJobType(job_types)

@advertisement.delete('/advertisement/{advertisement_id}')
async def delete(advertisement_id: str = Path(...)):
    return delete_advertisement(advertisement_id)

@advertisement.patch('/advertisement')
async def update(update: UpdateAdvertisement):
    return update_advertisement(update)
    
# @advertisement.get('/advertisements')
# async def get_all_advertisements():
#     return getAll()

