from typing import List
from fastapi import APIRouter, Path, Query
import urllib
from controller.advertisement import post_advertisement, getAdvertisementsByCustomer, getAdvertisementsByJobType, accept_advertisement, delete_advertisement, bid_advertisement, cancel_bid, cancel_job
from models.advertisement import AcceptAdvertisement, Advertisement, BidAdvertisement, CancelBid, CancelJob

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

@advertisement.patch('/advertisement/accept')
async def accept(update: AcceptAdvertisement):
    return accept_advertisement(update)

@advertisement.patch('/advertisement/bid')
async def bid(bid: BidAdvertisement):
    return bid_advertisement(bid)

@advertisement.patch('/advertisement/cancelBid')
async def bid(bid: CancelBid):
    return cancel_bid(bid)

@advertisement.patch('/advertisement/cancelJob')
async def bid(cancel: CancelJob):
    return cancel_job(cancel)
    
# @advertisement.get('/advertisements')
# async def get_all_advertisements():
#     return getAll()

